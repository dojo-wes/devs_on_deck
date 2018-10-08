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




class AllLanguageManager(models.Manager):
    #used by admin to add all languages to checkboxs for user to choose from
    def create_lang(self, form):
        error=[]

        if len(form['language']) == 0: 
            error.append("Language is blank")
        
        language=self.filter(name=form['language'])
        if len(language) > 0:
            error.append("This language already exists")
        
        if len(error) > 0:
            return error
        else:
            language=self.create(name=form['language'])
            return language

class AllLanguage(models.Model):
    name=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects= AllLanguageManager()

class LanguageManager(models.Manager):
    #adds bio to Developer
    def add_bio_and_langs(self, form, user_id):
        print "added lang,bio"
        user = Developer.object.get(id=user_id)

        error = []
        selected_languages = form.getlist('language')

        if len(form['short_bio']) < 1:
            error.append("Bio is blank. To skip this step, click Skip This Step")
            return error 
        if len(selected_languages) != 5:
            error.append("Please choose 5 languages. To skip this step, click Skip This Step")
            return error
        else:
            #dev_lang=self.create(lang_1=AllLanguage.objects.get(id=selected_languages[0], lang_2=AllLanguage.objects.get(id=selected_languages[1], lang_3=AllLanguage.objects.get(id=selected_languages[2], lang_4=AllLanguage.objects.get(id=selected_languages[3], lang_5=AllLanguage.objects.get(id=selected_languages[4], short_bio=form['short_bio'], developer=user)
            #return dev_lang

            dev_lang=self.create(lang_1=selected_languages[0], lang_2=selected_languages[1], lang_3=selected_languages[2], lang_4=selected_languages[3], lang_5=selected_languages[4], short_bio=form['short_bio'], developer=user)
            return dev_lang

class Language(models.Model):
    lang_1=models.IntegerField(null=True)
    lang_2=models.IntegerField(null=True)
    lang_3=models.IntegerField(null=True)
    lang_4=models.IntegerField(null=True)
    lang_5=models.IntegerField(null=True)
    short_bio=models.TextField(max_length=500, blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    all_languages=models.ForeignKey(AllLanguage, related_name="languages", null=True)
    developer=models.ForeignKey(Developer, related_name="dev_lang")
    objects= LanguageManager()


class AllFrameworkManager(models.Manager):
    #used by admin to add all languages to checkboxs for user to choose from
    def create_framework(self, form):
        error=[]

        if len(form['framework']) == 0: 
            error.append("Framework is blank")
        
        framework=self.filter(name=form['framework'])
        if len(framework) > 0:
            error.append("This framework already exists")
        
        if len(error) > 0:
            return error
        else:
            framework=self.create(name=form['framework'])
            return framework

class AllFramework(models.Model):
    name=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects= AllFrameworkManager()


class FrameworkManager(models.Manager):
    def add_frameworks(self, form, user_id):
        print "added frameworks"
        user = Developer.object.get(id=user_id)

        error = []
        selected_frameworks = form.getlist('frameworks')
        for framework in selected_frameworks:
            print framework

        if len(selected_frameworks) != 5:
            error.append("Please choose 5 languages. To skip this step, click Skip This Step")
            return error
        else:
            dev_frame=self.create(frame_1=selected_frameworks[0], frame_2=selected_frameworks[1], lang_3=selected_frameworks[2], lang_4=selected_frameworks[3], lang_5=selected_frameworks[4], developer=user)
            return dev_frame

class Framework(models.Model):
    frame_1=models.IntegerField(null=True)
    frame_2=models.IntegerField(null=True)
    frame_3=models.IntegerField(null=True)
    frame_4=models.IntegerField(null=True)
    frame_5=models.IntegerField(null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    all_frameworks=models.ForeignKey(AllFramework, related_name="frameworks", null=True)
    developer=models.ForeignKey(Developer, related_name="dev_frame")
    objects= FrameworkManager()