from django.urls import path
from django.conf import settings
from . import views



urlpatterns = [
    path('', views.LinkList.as_view(), name='link-list'),
    path('link-create/', views.LinkCreate.as_view(), name='link-create'),
    path('link-update/<str:pk>', views.LinkUpdate.as_view(), name='link-update'),
    path('delete/<str:pk>', views.delete, name='delete'),
    # path('new/', views.new, name='new'),
    # path('edit/<int:id>/', views.edit, name='edit'),
    # path('delete/<int:id>/', views.delete, name='delete'),
    # path('update/<int:id>/', views.update, name='update'),
    # path('table/<int:link_id>/', views.detail, name='detail'),
    # path('table/', views.table, name='table'),
    # path('<int:movie_id>/', views.movie),
    # path('upload/', views.upload, name='upload'),
    # path('link-list/', views.linkList, name='link-list'),
    # path('link-detail/<str:pk>', views.linkDetail, name='link-detail'),
    # path('link-create/', views.linkCreate, name='link-create'),
    # path('link-update/<str:pk>', views.linkUpdate, name='link-update'),
    # path('link-delete/<str:pk>', views.linkDelete, name='link-delete'),
    
    
]