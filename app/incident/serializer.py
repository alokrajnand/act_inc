from rest_framework import serializers
from .models import *
from rest_framework import exceptions


# ******************************************************************
# course serializer
# *******************************************************************

class IncidentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Incident
        fields = "__all__"
