from django.utils.functional import SimpleLazyObject
from django.urls import resolve
from django.http import HttpRequest


def current_path(request: HttpRequest):
    return {
        "current_path": request.path,
        "current_view": SimpleLazyObject(lambda: resolve(request.path).url_name)
    }
