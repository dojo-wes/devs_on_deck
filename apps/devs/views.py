# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from .models import Developer
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
            return redirect("devs:index")
    else:
        return redirect("devs:index")

def login(request):
    return render(request, 'devs/login.html')

def loginprocess(request):
    # if request.method == 'POST':
    pass
