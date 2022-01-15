import email
from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=40)
    mail = models.EmailField(max_length=254)
    clave = models.CharField(max_length=12)