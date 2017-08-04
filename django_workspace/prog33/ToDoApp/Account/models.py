# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
# a class GenericUser which will inherit the models.Model class of django
class GenericUser(models.Model):
    # columns in the table
    user_name = models.CharField( max_length=255, default=None)
    email = models.CharField( max_length=255, default=None)
    mobile_number = models.IntegerField( default=0)
    # for current date time storing use auto_now=true
    created_on = models.DateTimeField( auto_now=True)