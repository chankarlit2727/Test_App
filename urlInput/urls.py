from django.urls import path
from django.conf.urls import url
from django.conf import settings
from . import views

if 'heartbeat' in settings.INSTALLED_APPS:
  from heartbeat.urls import urlpatterns as heartbeat_urls

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('delete/<int:id>/', views.delete, name='delete'),
    # path('update/<int:id>/', views.update, name='update'),
    # path('table/<int:link_id>/', views.detail, name='detail'),
    # path('table/', views.table, name='table'),
    # path('<int:movie_id>/', views.movie),
    path('upload/', views.upload, name='upload'),
    
]