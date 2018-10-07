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
        new_bio = Language.objects.add_bio(request.POST, request.session['user_id'])    
        print new_bio
        #picked_languages = Language.objects.choose_languages(request.POST, request.session['user_id'], language_id)
        #print picked_languages
       
        #this works to retrieve language ids selected with checkboxes
        selected_languages = request.POST.getlist('language')
        for language in selected_languages:
            print language #will be id because form value is language.id
        
        print "*" * 30

        #this works to retrieve all language ids from AllLanguages
        all_languages = AllLanguage.objects.all()
        for lang in all_languages:
            print lang.id 

        #need to figure out the logic to match up the ids and save them to the variables in the Language class which is connected to the developer. Ideally this happens in models.py once Language.objects.choose_languages method works above. 

        '''
        lang_list = []
        for language in selected_languages:
            for lang in all_languages:
                if language == lang.id:
                    lang_list.append(language)
                    print lang_list
        
                    if lang_list == 5:
                        Language.objects.create(lang_1=language[0], lang_2=language[1], lang_3=language[2], lang_4=language[3], lang_5=language[4], short_bio=request.POST['short_bio'], developer=user)
                        print lang_list
        '''            
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
