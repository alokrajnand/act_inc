from django.db import models
from datetime import datetime
# Create your models here.
import datetime
# **********************************************************
# Course  Model
# *********************************************************
# current date and time


class Incident(models.Model):
    inc_number = models.CharField(max_length=50, unique=True, null=False)
    inc_for_route = models.CharField(max_length=50, unique=True, null=False)
    inc_created_by = models.CharField(max_length=50, unique=True, null=False)
    inc_closed_by = models.CharField(max_length=50, unique=True, null=True)
    inc_closing_remark = models.CharField(
        max_length=50, unique=True, null=True)
    inc_detail = models.CharField(max_length=50, null=False)
    inc_status = models.CharField(max_length=8, null=False)
    inc_priority = models.CharField(max_length=2, null=False)
    inc_open_dt = models.DateTimeField(
        default=datetime.datetime.now().replace(microsecond=0), null=False)
    inc_closed_dt = models.DateTimeField(
        default=datetime.datetime.now().replace(microsecond=0), null=True)

    def __str__(self):
        return self.__all__
