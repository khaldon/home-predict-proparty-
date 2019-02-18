from django.db import models
from django.urls import reverse
# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField( max_length=254)
    subject = models.CharField( max_length=50)
    message = models.TextField()

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse("contact:contact")
    