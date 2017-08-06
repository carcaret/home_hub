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
});

var videoHtml = '<video id="camera-stream" width="640" height="360" class="video-js vjs-default-skin" controls autoplay>' +
                    '<source src="http://192.168.0.160/hls/index.m3u8" type="application/x-mpegURL"/>' +
                '</video>';

function start() {
    if (!isVideoPresent()) {
        put('/camera/start/', async function() { 
                $('#stream-wrapper').html(videoHtml);
                await sleep(2000);
                videojs('camera-stream'); 
            });
    }
}

function sleep(ms) {
      return new Promise(resolve => setTimeout(resolve, ms));
}

function stop() {
    put('/camera/stop/', function() { 
        if (isVideoPresent()) {
            videojs('camera-stream').dispose();
        }
    });
}

function isVideoPresent() {
    return $('#stream-wrapper').children().length > 0;
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
