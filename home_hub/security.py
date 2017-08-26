import os

from base64 import b64decode

from functools import wraps

from django.conf import settings
from django.http import HttpResponse,HttpResponseForbidden
from django.contrib.auth import authenticate, login

def basic_auth_required(func):
    @wraps(func)
    def _decorator(request, *args, **kwargs):
        if 'HTTP_AUTHORIZATION' in request.META:
            authmeth, auth = request.META['HTTP_AUTHORIZATION'].split(' ', 1)
            if authmeth.lower() == 'basic':
                auth = b64decode(auth.strip()).decode('utf-8')
                username, password = auth.split(':', 1)
                if username == settings.USERNAME and password == settings.PASSWORD:
                    return func(request, *args, **kwargs)
                else:
                    return HttpResponseForbidden('<h1>Forbidden</h1>')
        res = HttpResponse()
        res.status_code = 401
        res['WWW-Authenticate'] = 'Basic'
        return res
    return _decorator

