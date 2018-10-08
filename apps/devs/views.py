# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from .models import Developer, Language, AllLanguage
from ..state.models import State
from django.contrib import messages


# Create your views here.
def index(request):
    if 'dev_id' not in request.session:
        return redirect('devs:register')

    if 'logged_in_status' not in request.session:
        return redirect('devs:register')
def register(request):
    context={
        "state":State.object.all()
    }
    return render(request, 'devs/register.html',context)

def create(request):
    if request.method == 'POST':
        dev=Developer.object.creating_developer(request.POST)
        if type(dev) == list:
            for err in dev:
                messages.error(request, err)
            return redirect("devs:index")
        else:
            request.session['user_id'] = dev.id
            return redirect("devs:languages")
    else:
        return redirect("devs:index")

def login(request):
    return render(request, 'devs/login.html')

def loginprocess(request):
    if request.method == 'POST':
        error = Developer.object.login_validation(request.POST)
        if type(error) == list:
            for err in error:
                messages.error(request, err)
            return redirect("devs:login")
        else:
            user_id = error
            print user_id
            return render(request, "devs/developers.html",)
    else:
        if "user_id" in request.session:
            return render(request, "devs/developers.html",)
        return redirect("devs:register")


def languages(request):

    context={
        "language": AllLanguage.objects.all(),
    }
    return render(request,'devs/languages.html', context)

def languageprocess(request):
    if request.method == 'POST':
        user = request.session['user_id']
        dev_lang = Language.objects.add_bio_and_langs(request.POST, request.session['user_id'])    
        print dev_lang.short_bio
        print dev_lang.lang_1
        print "*" * 30
        
        selected_languages = request.POST.getlist('language')

        all_languages = AllLanguage.objects.all()
        for language in all_languages:
            print language.id
            print language.name

        print "-" * 30

        for select_lang in selected_languages:
            print select_lang
        
        #doesn't work:
        if language.id == select_lang:
            print "match!"

        test = Language.objects.get(id=user)
        print test.developer.first_name
       
       
        return redirect('devs:frameworks')
        

def frameworks(request):
    #user_bio = request.POST['short_bio']
    bio_message = "Developers with a complete profile have a much higher chance of being considered for a position. Up your style and complete your profile."
    
    #if request.POST['short_bio']:
    progress = '66'
    #else:
    #    progress = '33'
    
    context = {
        #'user_bio': user_bio,
        'bio_message': bio_message,
        'progress': progress,
        #'error': error
        }
    return render(request, 'devs/frameworks.html', context)


   
def frameworksprocess(request):
    if request.method == 'POST':
        #new_frame = Framework.objects.add_framework(request.POST, request.session['user_id'])
        print new_frame
        return redirect('devs:dashboard')


def add_lang(request):
    return render(request, 'devs/add_lang.html')

def create_lang(request):
    if request.method == "POST":
        language=AllLanguage.objects.create_lang(request.POST)
        if type(language) == list:
            for err in language:
                messages.error(request, err)
            return redirect("devs:add_lang")
        else:
            print language.name
            print language.id
            return redirect("devs:languages")
    else:
        return redirect("devs:add_lang")

def logout(request):
    if request.method == "POST":
        request.session.clear()
        return redirect("devs:index")
    else:
        return render(request, "devs/developers.html")
