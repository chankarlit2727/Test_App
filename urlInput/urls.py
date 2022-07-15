from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('getLink/', views.getLink, name='getLink'),
    path('createLink/', views.CreateLink.as_view(), name='createLink'),
    path('updateLink/<pk>', views.UpdateLink.as_view(), name='updateLink'),
    path('deleteLink/<pk>', views.DeleteLink.as_view(), name='deleteLink'),

]