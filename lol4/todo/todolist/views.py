from django.shortcuts import render
from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse
from django.views.generic.base import View
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.paginator import Paginator
from django.shortcuts import render
import random
from random import randint
from todolist import models
def add_todo(request):
    if request.method == "POST":
        todo = models.todos()
        todo.doing = request.POST.get('doing')
        todo.time = request.POST.get('time')
        todo.save()
        return redirect('/')
    return render(request, 'addDolist.html')

class TodoView(View):
        
    def get(self, request):
        Todos = models.todos.objects.all()
        return render(request, 'index.html', {'todos':Todos})