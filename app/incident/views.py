
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
# Incident
# *******************************************************************

class IncidentViewSet(viewsets.ViewSet):
    permission_classes = [AllowAny]

    def getIncAll(self, request, format=None):
        data = Incident.objects.all()
        serializer = IncidentSerializer(data, many=True)
        return Response(serializer.data)

    def getIncByUser(self, request, name):
        data = Incident.objects.filter(inc_created_by=name)
        if (data.count() == 0):
            return Response({
                'message': 'No Data',
                'status': 400
            })
        else:
            serializer = IncidentSerializer(data, many=True)
            return Response(serializer.data)

    def getIncByStatus(self, request, name):
        data = Incident.objects.filter(inc_status=name)
        if (data.count() == 0):
            return Response({
                'message': 'No Data',
                'status': 400
            })
        else:
            serializer = IncidentSerializer(data, many=True)
            return Response(serializer.data)

    def getIncByUserStatus(self, request, name, status):
        data = Incident.objects.filter(
            inc_created_by=name).filter(inc_status=status)
        if (data.count() == 0):
            content = 'No Data in the table'
            return Response(content, status.HTTP_401_UNAUTHORIZED)
        else:
            serializer = IncidentSerializer(data, many=True)
            return Response(serializer.data)

    def postInc(self, request, format=None):
        json_parser = JSONParser()
        data = json_parser.parse(request)

        print('ok')
        serializer = IncidentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        else:
            return JsonResponse(serializer.errors, status=400)

    def put_incident(self, request, name, pk=None):
        inc = Incident.objects.get(id=name)
        serializer = IncidentSerializer(
            inc, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        else:
            return JsonResponse(serializer.errors, status=400)
