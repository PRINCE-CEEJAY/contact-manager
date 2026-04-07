from django import forms
from .models import ManagerModel

class ManagerForm(forms.ModelForm):
    class Meta:
        model = ManagerModel
        fields = ['name', 'email', 'bio']