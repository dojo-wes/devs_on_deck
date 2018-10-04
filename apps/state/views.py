# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,redirect,HttpResponse
from .models import State
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,"state/index.html")

def create(request):
    if request.method == "POST":
        state=State.object.create_state(request.POST)
        if type(state) == list:
            for err in state:
                messages.error(request, err)
            return redirect("state:index")
        else:
            print state
            return redirect("state:index")
    else:
        return redirect("devs:register")