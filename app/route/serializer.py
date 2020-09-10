from rest_framework import serializers
from .models import *
from rest_framework import exceptions


# ******************************************************************
# course serializer
# *******************************************************************

class RouteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Route
        fields = "__all__"
