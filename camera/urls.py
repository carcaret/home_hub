from django.conf.urls import url

from .views import CameraHomePage

urlpatterns = [
    url(r'^$', CameraHomePage.as_view()),
]
