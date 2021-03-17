from django.urls import path, re_path
from .views import index, create, update, delete, confirm, \
    ajax_basket, ajax_basket_display


urlpatterns = [
    path('', index),
    path('index', index),
    path('create', create),
    path('confirm', confirm),
    re_path(r'^update/(?P<id>[0-9]+)$', update),
    re_path(r'^delete/(?P<id>[0-9]+)$', delete),
    path('ajax_basket', ajax_basket),
    path('ajax_basket_display', ajax_basket_display),
]
