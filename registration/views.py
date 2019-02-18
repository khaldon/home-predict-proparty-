from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import TemplateView
from registration import forms 


class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('registration:login')
    template_name = 'registration/signup.html'

class HomePage(TemplateView):
    template_name = 'index.html'
class GalleryPage(TemplateView):
    template_name = 'gallery.html'
class PropertiesPage(TemplateView):
    template_name = 'properties.html'
class PropertiesDetailPage(TemplateView):
    template_name = 'properties-detail.html'
class BlogArchive(TemplateView):
    template_name = 'blog-archive.html'
class BlogSingle(TemplateView):
    template_name = 'predict-house.html'