from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.ContactView.as_view()),
    path('add', views.ContactView.create(views.ContactView, request=PO))
]