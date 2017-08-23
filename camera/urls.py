from django.conf.urls import url

from . import views 

urlpatterns = [
    url(r'^$', views.index),
    url(r'^start/', views.start),
    url(r'^stop/', views.stop),
    url(r'^enc.key', views.enckey),
]
