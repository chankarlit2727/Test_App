from django.urls import path
from django.conf import settings
from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('getUsers/', views.getUsers, name='getUsers'),
    path('createLink/', views.CreateLink.as_view(), name='createLink'),
    path('updateLink/<pk>', views.UpdateLink.as_view(), name='updateLink'),
    path('deleteLink/<pk>', views.DeleteLink.as_view(), name='deleteLink'),
    # path('', views.LinkList.as_view(), name='link-list'),
    # path('link-create/', views.LinkCreate.as_view(), name='link-create'),
    # path('link-update/<str:pk>', views.LinkUpdate.as_view(), name='link-update'),
    # path('delete/<str:pk>', views.delete, name='delete'),
    # path('new/', views.new, name='new'),
    # path('edit/<int:id>/', views.edit, name='edit'),
    # path('delete/<int:id>/', views.delete, name='delete'),
    # path('update/<int:id>/', views.update, name='update'),
    # path('table/<int:link_id>/', views.detail, name='detail'),
    # path('table/', views.table, name='table'),
    # path('upload/', views.upload, name='upload'),
    # path('link-list/<int:pk>', views.LinkDetail.as_view(), name="link-detail"),
    # path('link-list/', views.LinkList.as_view(), name='link-list'),
    # path('link-create/', views.LinkCreate.as_view(), name='link-create'),
]