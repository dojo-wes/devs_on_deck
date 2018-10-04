# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
import re, bcrypt

# Create your views here.
def index(request):
    if 'dev_id' not in request.session:
        return redirect('devs:register')

    if 'logged_in_status' not in request.session:
        return redirect('devs:register')
    
def register(request):
    return render(request, 'devs/register.html')

def create(request):
    # if request.method == 'POST':
    pass

def login(request):
    return render(request, 'devs/login.html')

def loginprocess(request):
    # if request.method == 'POST':
    pass
