from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    nome = models.CharField(max_length=155)
    

class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    capa = models.ImageField(default='', upload_to= './images')
    #Dentro da pasta Media vai ser criada images que armazenará esses itens
    publicação = models.DateField()
    paginas = models.IntegerField()
