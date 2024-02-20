from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.ContactView.as_view()),
    path('add', views.add_contact),
    path('edit/<int:id>', views.edit ),
    path('delete', views.delete),
    path('seria', views.seria),
]