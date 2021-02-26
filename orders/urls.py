from django.urls import path, re_path
from .views import index, create, update, delete


urlpatterns = [
    path('', index),
    path('index', index),
    path('create', create),
    re_path(r'^update/(?P<id>[0-9]+)$', update),
    re_path(r'^delete/(?P<id>[0-9]+)$', delete),
]
