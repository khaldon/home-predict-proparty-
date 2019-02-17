from django.shortcuts import render
from django.views.generic import CreateView
from . import models
# Create your views here.
class CreatContact(CreateView):
    model = models.Contact
    fields = all
    
