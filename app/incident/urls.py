from django.contrib import admin
from django.urls import path, include


from .views import *

urlpatterns = [
    path('', IncidentViewSet.as_view({'get': 'get'})),
    path('<name>/', IncidentViewSet.as_view({'get': 'get_user_inc'})),

]
