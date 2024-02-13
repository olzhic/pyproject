from django.shortcuts import render
from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .form import ContactsForm
from .models import Contacts
# Create your views here.


class ContactView(View):
    def create(self, request):
        form = ContactsForm(request.POST)
        if form.is_valid():
            form = form.save(commit = False)
            form.save()
        return redirect()
    
    def get(self, request):
        kontacts = Contacts.objects.all()
        return render(request, 'index.html', {'contacts':kontacts})