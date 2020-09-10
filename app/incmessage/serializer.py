from rest_framework import serializers
from .models import *
from rest_framework import exceptions


# ******************************************************************
# course serializer
# *******************************************************************

class IncMessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Incmessage
        fields = "__all__"
