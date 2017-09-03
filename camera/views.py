from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.conf import settings

from home_hub.security import if_authenticated

from .picam import isOn 
from .picam import start_picam
from .picam import stop_picam

@login_required
def index(request, *args, **kwargs):
    return render(request, 'index.html', {'stream_url': settings.STREAM_URL})

@if_authenticated
def status(request):
    if request.method == 'GET':
        return JsonResponse({'isOn': isOn()})
    else:
        return HttpResponse(status=405) 

@if_authenticated
def start(request):
    if request.method == 'PUT':
        start_picam()
        return JsonResponse({'message': 'Started!'})
    else:
        return HttpResponse(status=405) 

@if_authenticated
def stop(request):
    if request.method == 'PUT':
        stop_picam()
        return JsonResponse({'message': 'Stopped!'})
    else:
        return HttpResponse(status=405) 

@if_authenticated
def enckey(request):
    if request.method == 'GET':
        return HttpResponse(bytes.fromhex(settings.STREAM_KEY), content_type='application/octet-stream')
    else:
        return HttpResponse(status=405)
