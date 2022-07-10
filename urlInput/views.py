from django.shortcuts import redirect, render, get_object_or_404
from django.http import Http404, HttpResponse

import urlInput
from .forms import UploadForm, PostForm
from .models import Movie
from .models import Link
from django.contrib import messages
from django.views import generic
from .auth import auth
from .settings import HEARTBEAT
import json
from collections import OrderedDict
from importlib import import_module
from django.core import serializers
import requests
from django.utils import timezone


def new(request):
    if request.method == "POST":
            form = PostForm(request.POST)
            if form.is_valid():
                try:
                    form.save()
                    return redirect("/urlInput/")
                except:
                    pass
    else:
        form = PostForm()
        return render(request, "urlInput/index.html", {"form": PostForm })

def index(request):
    link_list = Link.objects.all()
    return render(request, 'urlInput/show.html', {'link_list': link_list})

def edit(request, id):
    link = Link.objects.get(id=id)
    return render(request, 'urlInput/edit.html', {'link':link})

def update(request, id):
    link = Link.objects.get(id=id)  
    form = PostForm(request.POST, instance = link)  
    if form.is_valid(): 
        form.save(commit=True)  
        return redirect("/urlInput/")  
    return render(request, 'urlInput/edit.html', {'link': link})  

def delete(request, id):
    link = Link.objects.get(id=id)
    link.delete()
    return redirect("/urlInput/")



def upload(request):
    if request.POST:
        form = UploadForm(request.POST, request.FILES)
        print(request.FILES)
        if form.is_valid():
            form.save()
        return redirect(index)
    return render(request, 'urlInput/upload.html', {'form': UploadForm})

def movie(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    if movie is not None:
        return render(request, 'urlInput/movie.html', {'movie' : movie})
    else:
        raise Http404('Movie does not exist')

