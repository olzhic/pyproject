from django.shortcuts import render
from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse
from django.views.generic.base import View
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .form import ContactsForm
from .models import Contacts
from .serial import ContactSerializer
from django.core.paginator import Paginator
from django.shortcuts import render
import random
from random import randint

# Create your views here.
def randomize(request):
    randNumber = 0
    if request.method == "POST":
        a = request.POST.get("a")
        b = request.POST.get("b")
        randNumber = randint(int(a), int(b))
    
    return render(request, "random.html", {"randNumber":randNumber})
def listing(request):
    contact_list = Contacts.objects.all()
    paginator = Paginator(contact_list, 25) 

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "list.html", {"page_obj": page_obj})

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username = username, password = password)
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


    
    
@login_required
def add_contact(request):
    if request.method == "POST":
        contact = Contacts()
        contact.name = request.POST.get('name')
        contact.number = request.POST.get('phone')
        contact.save()
        return redirect('/')
    return render(request, 'addPhone.html')
   

class ContactView(View):
        
    
    def get(self, request):
        kontacts = Contacts.objects.all()
        return render(request, 'index.html', {'contacts':kontacts})
    
@login_required
def edit(request, id):
    try:
        contact = Contacts.objects.get(id=id)
        if request.method == "POST":
            contact.name = request.POST.get('name')
            contact.number = request.POST.get('number')
            contact.save()
            return HttpResponseRedirect('/')
        else:
            return render(request, "edit.html", {"cont":contact})
    except Contacts.DoesNotExist:
        return HttpResponse('<h1> Person not found </h1>')
    
@login_required
def delete(request, id):
    try:
        contact = Contacts.objects.get(id=id)
        contact.delete()
        return HttpResponseRedirect('/')
    except Contacts.DoesNotExist:
        return HttpResponse('<h1> Product does not exist imbecile </h1>')
    
@login_required
def seria(request, id):
    order = Contacts.objects.get(id=id)
    serializer = ContactSerializer(order)
    return HttpResponse(f'{serializer.data}')

@login_required
def search(request):
    if request.method == "POST":
        nameOrnumber = str(request.POST.get("name"))
        if nameOrnumber.isdigit():
            try:
                name = Contacts.objects.get(number = nameOrnumber)
                serializer = ContactSerializer(name)
                return HttpResponse(f'{serializer.data}')
            except:
                return HttpResponse('<h1>poshel nahui</h1>')
        else:
            try:
                name = Contacts.objects.get(name = nameOrnumber)
                serializer = ContactSerializer(name)
                return HttpResponse(f'{serializer.data}')
            except:
                return HttpResponse('<h1>poshel nahui</h1>')
    return render(request, "contactFinder.html")