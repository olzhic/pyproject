from .models import Contacts
from django import forms

class ContactsForm(forms.ModelForm):
    class Meta:
        model = Contacts
        fields = {'name', 'number'}