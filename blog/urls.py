from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.PostView.as_view()),
    path('<int:pk>/', views.PostDetail.as_view()),
    path('review/<int:pk>/', views.AddComments.as_view(), name = 'add_comments'),
    path('review/<int:pk>/', views.AddComments.as_view(), name = 'add_like'),
    path('register/', views.register, name = 'register'),
]
