from django.views.generic import CreateView
from . import forms 
from .models import Contact
from django.http import HttpResponse
from django.urls import reverse_lazy
from django_ajax.mixin import AJAXMixin
from django.contrib import messages

# Create your views here.
class CreatContact(AJAXMixin,CreateView):
    ajax_mandatory = False
    form_class = forms.CreatContactForm
    template_name = 'contact.html'
    def form_valid(self, form):
        self.object = form.save()
        messages.success(self.request, 'Thank you for register')
        return super().form_valid(form)