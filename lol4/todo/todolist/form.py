from .models import todos
from django import forms

class TodoForm(forms.ModelForm):
    class Meta:
        model = todos
        fields = {'doing', 'time'}