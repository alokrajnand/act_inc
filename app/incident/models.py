from django.db import models
from datetime import datetime
# Create your models here.
from django.utils import timezone
# **********************************************************
# Course  Model
# *********************************************************


class Incident(models.Model):
    inc_status = models.CharField(max_length=50, null=False)
    inc_route_name = models.CharField(max_length=100,  null=False)
    inc_route_id = models.CharField(max_length=30, null=False)
    inc_created_by = models.CharField(max_length=50, null=False)
    inc_short_desc = models.CharField(max_length=100, null=True)
    inc_created_dt = models.DateTimeField(default=timezone.now, null=False)
    inc_closed_dt = models.DateTimeField(null=True)
    inc_closed_by = models.CharField(max_length=50, null=True)
    inc_updated_dt = models.DateTimeField(default=timezone.now, null=True)

    def __str__(self):
        return self.__all__
