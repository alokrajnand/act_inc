from django.db import models


from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)
from django.core.validators import RegexValidator
# write the code of user manager
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from datetime import datetime
from userauth.models import *

# **********************************************************
# User Profile model and processing
# *********************************************************


class Profile(models.Model):
    phone_number = models.OneToOneField(
        User, to_field='email_address', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.__all__
