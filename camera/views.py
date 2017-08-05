from django.views.generic import TemplateView
from django.http import JsonResponse 

class CameraHomePage(TemplateView):
    template_name = 'index.html'

def start(request):
    return JsonResponse({'message': 'Started!'})

def stop(request):
    return JsonResponse({'message': 'Stopped!'})
