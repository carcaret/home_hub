from django.conf.urls import url

from .views import VideoHomePage

urlpatterns = [
    url(r'^$', VideoHomePage.as_view()),
]
