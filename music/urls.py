"""blogwebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from . import views

#  app_name used for Namespace 

app_name = 'music'

urlpatterns = [

    path('', views.IndexView.as_view(), name='index'),

    path('<int:pk>/', views.AlbumDetail.as_view(), name='detail'),

    path('album/add/', views.AlbumCreate.as_view(), name='album_create'),

    path('album/edit/<int:pk>/', views.AlbumUpdate.as_view(), name='album_update'),

    path('album/delete/<int:pk>/', views.AlbumDelete.as_view(), name='album_delete'),


    


]

