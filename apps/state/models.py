# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.

class StateManager(models.Manager):
    def create_state(self,form):
        error=[]

        if len(form['state']) == 0 or len(form['state']) < 2:
            error.append("Enter a proper state")

        state=self.filter(name=form['state'])
        if len(state) > 0:
            error.append("This State already exist")

        if len(error) > 0:
            return error
        else:
            state=self.create(name=form['state'])
            return state

class State(models.Model):
    name=models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    object=StateManager()