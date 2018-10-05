# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from ..state.models import State
# Create your models here.
import bcrypt
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your models here.

class DeveloperManager(models.Manager):

    def creating_developer(self,form):
        print "here"
        error = []

        if len(form['first_name']) < 2:
            error.append("first_name must be atleast 3 character(s)")
        if len(form['last_name']) < 2:
            error.append("last_name should be atleast 3 character(s)")
        if len(form['address1']) < 2:
            error.append("address should be atleast 3 character(s)")
        if len(form['city']) == 0:
            error.append("city should'nt be empty")
        if len(form['state']) == 0:
            error.append("state should'nt be empty")
        if not EMAIL_REGEX.match(form['email']):
            error.append("Invalid Email Typed")
        if len(form['password']) < 2:
            error.append("Password must be 8 character(s)")
        if form['confirm_password'] != form['password']:
            error.append("Confirm Password again!!")

        check_email = self.filter(email=form['email'])
        if len(check_email) != 0:
            error.append("Invalid email")

        if len(error) > 0:
            return error
        else:
            hash1 = bcrypt.hashpw(form['password'].encode(), bcrypt.gensalt())
            created=self.create(first_name=form['first_name'], last_name=form['last_name'],address=form['address1'],city=form['city'], state=State.object.get(id=form['state']),email=form['email'], password=hash1)
            return created

    def login_validation(self, form_data):

        email = form_data['email']
        password = form_data['password']
        error = []

        if len(email) == 0 or len(password) == 0:
            error.append("Invalid Email or Password")
            return error

        user = self.filter(email=email)
        if len(user) == 0:
            error.append("Invalid Email or Password")
            return error

        user1 = user[0]
        if not bcrypt.checkpw(password.encode(), user1.password.encode()):
            error.append("Invalid Email or Password")
            return error
        else:
            return user1.id

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
    object= DeveloperManager()