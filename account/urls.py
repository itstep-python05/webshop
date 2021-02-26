from django.urls import path
from .views import entry, logout, reg


urlpatterns = [
    path('entry/', entry),
    path('logout/', logout),
    path('reg/', reg),
]