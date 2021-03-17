from django.urls import path, re_path
from .views import index, create, details, update, delete, select, ajax_select

urlpatterns = [
    path('', index),
    path('index', index),
    path('create', create),
    path('ajax_select', ajax_select),
    re_path(r'^details/(?P<id>[0-9]+)$', details),
    re_path(r'^update/(?P<id>[0-9]+)$', update),
    re_path(r'^delete/(?P<id>[0-9]+)$', delete),
    re_path(r'^select/(?P<cid>[0-9]+)$', select),
]
