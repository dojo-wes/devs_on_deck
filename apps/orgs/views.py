# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
import re, bcrypt

# Create your views here.
def index(request):
    if 'org_id' not in request.session:
        return redirect('orgs:register')

    if 'logged_in_status' not in request.session:
        return redirect('orgs:register')
    # return render(request, 'orgs/register.html')

def register(request):
    return render(request, 'orgs/register.html')


def create(request):
    # if request.method == 'POST':
    pass


def login(request):
    return render(request, 'orgs/login.html')


def loginprocess(request):
    # if request.method == 'POST':
    pass