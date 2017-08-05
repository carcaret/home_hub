from django.conf.urls import url

from . import views 

urlpatterns = [
    url(r'^$', views.CameraHomePage.as_view()),
    url(r'^start/', views.start),
    url(r'^stop/', views.stop),
]
