from django.db import models
from datetime import datetime
# Create your models here.
from django.utils import timezone
# **********************************************************
# Course  Model
# *********************************************************


class Route(models.Model):
    route_name = models.CharField(max_length=30, null=False)
    route_short_desc = models.CharField(max_length=100, null=True)
    route_start_point = models.CharField(max_length=100,  null=False)
    route_end_point = models.CharField(max_length=100,  null=False)
    route_state = models.CharField(max_length=100,  null=True)
    route_country = models.CharField(max_length=100,  null=True)
    route_city = models.CharField(max_length=100,  null=True)
    route_created_by = models.CharField(max_length=50, null=False)
    route_created_dt = models.DateTimeField(default=timezone.now, null=False)
    route_updated_dt = models.DateTimeField(default=timezone.now, null=True)

    def __str__(self):
        return self.__all__
