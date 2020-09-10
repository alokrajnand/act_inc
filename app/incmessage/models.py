from django.db import models
from datetime import datetime
# Create your models here.
from django.utils import timezone
# **********************************************************
# Course  Model
# *********************************************************


class Incmessage(models.Model):
    inc_id = models.CharField(max_length=50, null=False)
    text = models.CharField(max_length=300,  null=False)
    text_by = models.CharField(max_length=50, null=False)
    text_created_dt = models.DateTimeField(default=timezone.now, null=False)

    def __str__(self):
        return self.__all__
