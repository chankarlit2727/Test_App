from re import I
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic.edit import UpdateView
from django.http import Http404, HttpResponse, HttpResponseRedirect
from .forms import UploadForm
from .models import Movie
from .models import Link
import requests
from rest_framework import status, generics, mixins
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import LinkSerializer

from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK,HTTP_400_BAD_REQUEST

class LinkList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'urlInput/show.html'

    def get(self, request):
        queryset = Link.objects.all()
        return Response({'full_list': queryset})

class LinkCreate(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'urlInput/create.html'
    style = {'template_pack': 'rest_framework/vertical/'}

    def get(self, request):
        serializer = LinkSerializer()
        return Response({'serializer': serializer, 'style': self.style})

    def post(self, request):
        serializer = LinkSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            try:
                text = serializer.validated_data['link_text']
                r = requests.get(text)
                r1 = r.status_code
                if r1 == 200: 
                    serializer.validated_data['link_status_code'] = True
                    serializer.save()
                    return Response({'serializer': serializer, status:HTTP_200_OK})
                return redirect("/urlInput/")
            except requests.exceptions.RequestException as err:
                serializer.validated_data['link_status_code'] = False
                serializer.save()
                return Response({'serializer': serializer, status:HTTP_400_BAD_REQUEST})
        return redirect("/urlInput/")
        
        

class LinkUpdate(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'urlInput/updates.html'
    style = {'template_pack': 'rest_framework/vertical/'}

    def get(self, request, pk):
        link = get_object_or_404(Link, pk=pk)
        serializer = LinkSerializer(link)
        return Response({'serializer': serializer, 'link': link})

    def post(self, request, pk):
        link = get_object_or_404(Link, pk=pk)
        serializer = LinkSerializer(link, data=request.data)
        if serializer.is_valid(raise_exception=True):
            try:
                text = serializer.validated_data['link_text']
                r = requests.get(text)
                r1 = r.status_code
                if r1 == 200: 
                    serializer.validated_data['link_status_code'] = True
                    serializer.save()
                    return redirect("/urlInput/")
                return Response({'serializer': serializer, status:HTTP_200_OK})
                    
            except requests.exceptions.RequestException as err:
                serializer.validated_data['link_status_code'] = False
                serializer.save()
                return redirect("/urlInput/")
            
        



def delete(request, pk):
    link = Link.objects.get(pk=pk)
    link.delete()
    return redirect("/urlInput/")















# def list(request):
#     return render(request, "urlInput/list.html")


# @api_view(['GET'])
# def apiOverview(request):
#     api_urls = {

#     }

# @api_view(['GET'])
# def linkList(request):
#     link = Link.objects.all()
#     serializer = LinkSerializer(link, many=True)
#     return Response(serializer.data)

# @api_view(['GET'])
# def linkDetail(request,pk):
#     link = Link.objects.get(id=pk)
#     serializer = LinkSerializer(link, many=False)
#     return Response(serializer.data)

# @api_view(['POST'])
# def linkCreate(request):
#     serializer = LinkSerializer(data = request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)

# @api_view(['POST'])
# def linkUpdate(request, pk):
#     link = Link.objects.get(id=pk)
#     serializer = LinkSerializer(instance=link, data = request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)

# @api_view(['DELETE'])
# def linkDelete(request, pk):
#     link = Link.objects.get(id=pk)
#     link.delete()
#     return Response("Successfully Delete")

# def new(request):
#     if request.method == "POST":
#             form = PostForm(request.POST)
#             if form.is_valid():
#                 try:
#                     data = form.cleaned_data.get("link_text")
#                     r = requests.get(data)
#                     r1 = r.status_code
#                     if r1 == 200:
#                         obj = form.save(commit=False)
#                         obj.link_status_code = '200'
#                         print(vars(obj))
#                         obj.save()
#                         return redirect("/urlInput/")
#                 except requests.exceptions.RequestException as err:
#                     obj = form.save(commit=False)
#                     obj.link_status_code = '404'
#                     obj.save()
#                     print(vars(obj))
#                     return redirect("/urlInput/")
#     else:
#         form = PostForm()
#         return render(request, "urlInput/index.html", {"form": PostForm })

# def index(request):
#     link_list = Link.objects.all()
#     return render(request, 'urlInput/show.html', {'link_list': link_list})

# def edit(request, id):
#     link = get_object_or_404(Link,id=id)
#     return render(request, 'urlInput/edit.html', {'link':link})

# def update(request, id):
#     link = get_object_or_404(Link,id=id)
#     form = PostForm(request.POST, instance = link)
#     if form.is_valid():
#         try:
#             obj = form.save(commit=False)
#             data = form.cleaned_data.get("link_text")
#             r = requests.get(data)
#             r1 = r.status_code
#             if r1 == 200:
#                 link.link_status_code = '200'
#                 obj.save(update_fields=['link_text','link_status_code'])
#                 print(vars(obj))
#                 return redirect("/urlInput/")
#         except requests.exceptions.RequestException as err:
#             obj = form.save(commit=False)
#             link.link_status_code = '404'
#             obj.save(update_fields=['link_text','link_status_code'])
#             print(vars(obj))
#             return redirect("/urlInput/")
#     else:
#         print(form.errors.as_data())
#     return render(request, 'urlInput/edit.html', {'link': link})  

# def delete(request, id):
#     link = Link.objects.get(id=id)
#     link.delete()
#     return redirect("/urlInput/")  



# def upload(request):
#     if request.POST:
#         form = UploadForm(request.POST, request.FILES)
#         print(request.FILES)
#         if form.is_valid():
#             form.save()
#         return redirect(index)
#     return render(request, 'urlInput/upload.html', {'form': UploadForm})

# def movie(request, movie_id):
#     movie = Movie.objects.get(pk=movie_id)
#     if movie is not None:
#         return render(request, 'urlInput/movie.html', {'movie' : movie})
#     else:
#         raise Http404('Movie does not exist')

