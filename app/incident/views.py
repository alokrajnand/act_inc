
# this is for login and logout authentication
from rest_framework.renderers import JSONRenderer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from django.contrib.auth import login as django_login
from rest_framework.views import APIView
from django.shortcuts import render
# this is to send response to client
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt  # to resolve csrf issue
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
# model and serializer import
from .serializer import *
from .models import *
from django.core.mail import send_mail


# ******************************************************************
# Course
# *******************************************************************

class IncidentViewSet(viewsets.ViewSet):
    permission_classes = [AllowAny]

    def get(self, request, format=None):
        data = Incident.objects.all()
        serializer = IncidentSerializer(data, many=True)
        return Response(serializer.data)

    def get_user_inc(self, request, name):
        data = Incident.objects.filter(inc_created_by=name)
        if (data.count() == 0):
            return Response({
                'message': 'No Data',
                'status': 400
            })
        else:
            serializer = IncidentSerializer(data, many=True)
            return Response(serializer.data)
