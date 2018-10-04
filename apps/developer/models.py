# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from ..state.models import State
import bcrypt
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your models here.

class Developer(models.Model):
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    password=models.CharField(max_length=500)
    address=models.CharField(max_length=500)
    city=models.CharField(max_length=255)
    state=models.ForeignKey(State,related_name="state")
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)