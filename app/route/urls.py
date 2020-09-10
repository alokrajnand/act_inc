from django.contrib import admin
from django.urls import path, include


from .views import *

urlpatterns = [
    path('', RouteViewSet.as_view({'get': 'getRouteAll'})),
    path('<name>', RouteViewSet.as_view({'get': 'getRouteDetail'})),
]
