from django.shortcuts import redirect, render, get_object_or_404
from django.http import Http404, HttpResponse
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

def home(request):
    return HttpResponse("Ok")

# class TableView(generic.ListView):
#     template_name = 'urlInput/table.html'
#     context_object_name = 'latest_link_list'

#     def get_queryset(self):
#         """Return the last five published questions."""
#         return Link.objects.all()

# class DetailView(generic.DetailView):
#     model = Link
#     template_name = 'urlInput/detail.html'

def detail(request, link_id):
    link = get_object_or_404(Link, pk=link_id)
    return render(request, 'urlInput/detail.html', {'link': link})

# def view_info(request):
#     objs=Link.objects.all()
#     return render(request,'template_name',{'objs':objs})

def delete(request, link_id):
    link = get_object_or_404(Link, pk=link_id)
    link.delete()
    messages.warning(request, f'Link deleted!')
    return redirect("/")

def index(request):
    # latest_link_list = Link.objects.order_by('-link_status')
    # context = {'latest_link_list': latest_link_list}
    # return render(request, 'urlInput/index.html', context)
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Link Created!')

            return redirect("/urlInput/")
                
    else:
        form = PostForm()
        latest_link_list = Link.objects.all()
        return render(request, "urlInput/new.html", {"form": PostForm , "latest_link_list": latest_link_list})
        

def table(request):
    # if request.method == "POST":
    #     form = PostForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         messages.success(request, f'Link Created!')
    #         return redirect("/urlInput/new/")
                
    # else:
    #     form = PostForm()
    # return render(request, "urlInput/new.html", {"form": PostForm })
    latest_link_list = Link.objects.all()
    context = {'latest_link_list': latest_link_list}
    return render(request, 'urlInput/index.html', context)

def upload(request):
    if request.POST:
        form = UploadForm(request.POST, request.FILES)
        print(request.FILES)
        if form.is_valid():
            form.save()
        return redirect(home)
    return render(request, 'urlInput/upload.html', {'form': UploadForm})

def movie(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    if movie is not None:
        return render(request, 'urlInput/movie.html', {'movie' : movie})
    else:
        raise Http404('Movie does not exist')


def indexx(request):
    return HttpResponse(content='all good in the hood')


@auth
def details(request):
    response = {}
    for checker in HEARTBEAT['checkers']:
        checker_module = import_module(checker)
        checker_name = checker_module.__name__.split('.')[-1]
        data = checker_module.check(request)
        response.update({checker_name: data})

    data = OrderedDict(sorted(response.items()))

    return HttpResponse(json.dumps(data), content_type="application/json")