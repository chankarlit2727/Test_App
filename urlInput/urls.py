from django.urls import path
from django.conf import settings
from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('getUsers/', views.getUsers, name='getUsers'),
    path('createLink/', views.CreateLink.as_view(), name='createLink'),
    path('updateLink/<pk>', views.UpdateLink.as_view(), name='updateLink'),
    path('deleteLink/<pk>', views.DeleteLink.as_view(), name='deleteLink'),

]