from django import forms
from .models import FoundItem

class  FoundForm(forms.ModelForm):
    class Meta:
        model = FoundItem
        fields = ['title','description','contact_number','location','date_found','image']