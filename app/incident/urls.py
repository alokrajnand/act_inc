from django.contrib import admin
from django.urls import path, include


from .views import *

urlpatterns = [
    path('', IncidentViewSet.as_view({'get': 'getIncAll', 'post': 'postInc'})),
    path('<name>/', IncidentViewSet.as_view({'get': 'getIncByUser'})),
    path('status/<name>/', IncidentViewSet.as_view({'get': 'getIncByStatus'})),
    path('<name>/<status>/',
         IncidentViewSet.as_view({'get': 'getIncByUserStatus'})),
    path('update/<name>',
         IncidentViewSet.as_view({'put': 'put_incident'}))
]
