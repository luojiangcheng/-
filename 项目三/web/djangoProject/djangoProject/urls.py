"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path

from app import views

urlpatterns = [
    path('index/', views.index, name="index"),
    path('todo1/', views.todo1, name="todo1"),
    path('todo2/', views.todo2, name="todo2"),
    path('todo3/', views.todo3, name="todo3"),
    path('todo4/', views.todo4, name="todo4"),
    path('todo5/', views.todo5, name="todo5"),
    path('todo6/', views.todo6, name="todo6"),

]
