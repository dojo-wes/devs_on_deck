# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from ..state.models import State
from .models import Organization

import re, bcrypt

# Create your views here.
def index(request):
    if 'org_id' not in request.session:
        return redirect('orgs:register')

    if 'logged_in_status' not in request.session:
        return redirect('orgs:register')
    # return render(request, 'orgs/register.html')

def register(request):
    context = {
        "state": State.object.all()
    }
    return render(request, 'orgs/register.html',context)

def create(request):
    if request.method == 'POST':
        org = Organization.object.creating_organization(request.POST)
        if type(org) == list:
            for err in org:
                messages.error(request, err)
            return redirect("orgs:index")
        else:
            print org
            return render(request, "orgs/display_developers.html",)
    else:
        return redirect("orgs:index")


def login(request):
    return render(request, 'orgs/login.html')


def loginprocess(request):

    if request.method == 'POST':
        error = Organization.object.login_validation(request.POST)
        if type(error) == list:
            for err in error:
                messages.error(request, err)
            return redirect("orgs:login")
        else:
            user_id = error
            return render(request, "orgs/display_developers.html",)
    else:
        if "user_id" in request.session:
            return render(request, "orgs/display_developers.html",)
        return redirect("orgs:register")

def logout(request):
    if request.method == "POST":
        request.session.clear()
        return redirect("orgs:index")
    else:
        return render(request, "orgs/display_developers.html")

