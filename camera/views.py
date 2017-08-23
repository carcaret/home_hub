import os
import configparser

from django.utils.decorators import method_decorator 
from django.views.decorators.csrf import ensure_csrf_cookie 
from django.views.generic import TemplateView
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.conf import settings

from home_hub.security import basic_auth_required

from .picam import start_picam
from .picam import stop_picam

config = configparser.ConfigParser()
config.read(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir, 'security.ini'))

@basic_auth_required 
@ensure_csrf_cookie
def index(request, *args, **kwargs):
    return render(request, 'index.html', {'stream_url': settings.STREAM_URL})

def status(request):
    if request.method == 'GET':
        return JsonResponse({'isOn': isOn()})
    else:
        return HttpResponse(status=405) 

@basic_auth_required
def start(request):
    if request.method == 'PUT':
        start_picam()
        return JsonResponse({'message': 'Started!'})
    else:
        return HttpResponse(status=405) 

@basic_auth_required
def stop(request):
    if request.method == 'PUT':
        stop_picam()
        return JsonResponse({'message': 'Stopped!'})
    else:
        return HttpResponse(status=405) 

@basic_auth_required
def enckey(request):
    if request.method == 'GET':
        return HttpResponse(bytes.fromhex(config['STREAM']['key']), content_type='application/octet-stream')
    else:
        return HttpResponse(status=405)
