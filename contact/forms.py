from django import forms 
from . import models
#Create your views here.
class CreatContactForm(forms.ModelForm):
    class Meta:
        model = models.Contact
        fields = '__all__'
