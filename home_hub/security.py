from functools import wraps

from django.http import HttpResponse

def if_authenticated(func):
    @wraps(func)
    def _decorator(request, *args, **kwargs):
        if request.user.is_authenticated:
            return func(request, *args, **kwargs)
        else:
            return HttpResponse(status=401)
    return _decorator

