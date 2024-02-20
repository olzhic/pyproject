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
# Create your views here.


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
    
#@login_required
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
    
#@login_required
def delete(request, id):
    try:
        contact = Contacts.objects.get(id=id)
        contact.delete()
        return HttpResponseRedirect('/')
    except Contacts.DoesNotExist:
        return HttpResponse('<h1> Product does not exist imbecile </h1>')
    
#@login_required
def seria(request, id):
    order = Contacts.objects.get(id=id)
    serializer = ContactSerializer(order)
    return HttpResponse(f'{serializer.data}')