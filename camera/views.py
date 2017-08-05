from django.utils.decorators import method_decorator 
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.generic import TemplateView
from django.shortcuts import render
from django.http import HttpResponse 
from django.http import JsonResponse 

from .picam import stop_picam

class CameraHomePage(TemplateView):
    
    @method_decorator(ensure_csrf_cookie)
    def get(self, request, **kwargs):
        return render(request, 'index.html', {})

def start(request):
    if request.method == 'PUT':
        return JsonResponse({'message': 'Started!'})
    else:
        return HttpResponse(status=405) 

def stop(request):
    if request.method == 'PUT':
        stop_picam()
        return JsonResponse({'message': 'Stopped!'})
    else:
        return HttpResponse(status=405) 
