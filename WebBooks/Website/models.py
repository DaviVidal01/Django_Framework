from django.db import models

# Create your models here.
    
class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    capa = models.ImageField(default='', upload_to= './images')
    #Dentro da pasta Media vai ser criada images que armazenará esses itens
    publicação = models.DateField()
    paginas = models.IntegerField()
