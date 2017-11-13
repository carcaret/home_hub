$(document).ready(function() {
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
                // Send the token to same-origin, relative URLs only.
                // Send the token only if the method warrants CSRF protection
                // Using the CSRFToken value acquired earlier
                xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
            }
        }
    });
    checkStatus(function(input) { updateLeds(input) });
    initSocket();
});

function checkStatus(callback) {
    $.ajax({
        url: '/camera/status',
        type: 'GET',
        success: function(data) {
            callback(data.isOn);
        }
    });
}

function initSocket() {
    var socket = new WebSocket('ws://' + window.location.host + '/camera/');

    socket.onopen = function open() {
        console.log('WebSockets connection created.');
    };

    if (socket.readyState == WebSocket.OPEN) {
        socket.onopen();
    }

    socket.onmessage = function message(event) {
        var data = JSON.parse(event.data);
        document.getElementById('sound').setAttribute('level', data.value);
    }
}

function updateLeds(isOn) {
    if(isOn == true) {
        $('#led-green').removeClass().addClass('led-green');
        $('#led-red').removeClass().addClass('led-disabled');
    } else {
        $('#led-green').removeClass().addClass('led-disabled');
        $('#led-red').removeClass().addClass('led-red');
    }
}

function start() {
    put('/camera/start/', async function() {
        await sleep(2000); // we give time for picam to start streaming
        var streamUrl = $("#stream-url").val(); 
        videojs('camera-stream').src({
            src: streamUrl,
            type: 'application/x-mpegURL'
        });
        updateLeds(true);
    });
}

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

function stop() {
    videojs('camera-stream').reset();
    put('/camera/stop/', function() {});
    updateLeds(false);
}

function put(url, callback) {
    $.ajax({
        url: url,
        type: 'PUT',
        success: function(data) {
            callback();
        }
    });
}

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

function sameOrigin(url) {
    // test that a given url is a same-origin URL
    // url could be relative or scheme relative or absolute
    var host = document.location.host; // host + port
    var protocol = document.location.protocol;
    var sr_origin = '//' + host;
    var origin = protocol + sr_origin;
    // Allow absolute or scheme relative URLs to same origin
    return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
        (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
        // or any other URL that isn't scheme relative or absolute i.e relative.
        !(/^(\/\/|http:|https:).*/.test(url));
}
