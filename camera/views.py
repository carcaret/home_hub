from django.shortcuts import render
from django.views.generic import TemplateView

class CameraHomePage(TemplateView):
    template_name = 'index.html'
