from django.contrib import admin
from django.urls import path, include


from .views import *

urlpatterns = [
    path('<name>/', IncMessageViewSet.as_view(
        {'get': 'getMessageByInc', 'post': 'postMessage'})),
    path('', IncMessageViewSet.as_view({'post': 'postMessage'})),

]
