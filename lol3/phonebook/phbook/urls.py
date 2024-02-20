from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.ContactView.as_view()),
    path('add', views.add_contact),
    path('edit/<int:id>', views.edit ),
    path('delete/<int:id>', views.delete),
    path('seria', views.seria),
    path('search', views.search),
    path('register/', views.register, name = 'register'),
    path('login/', auth_views.LoginView.as_view(), name ='login'),
    path('logout/', auth_views.LogoutView.as_view(), name = 'logout'),
]