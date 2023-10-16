from django.shortcuts import render
from .models import Livro
# Create your views here.

def lista_livros(request):
    livros = Livro.objects.all()
    return render(request, 'lista_livros.html', {'livros': livros})

def livro_detalhes(request):
    livros = Livro.objects.all()
    return render(request, 'livro_detalhes.html', {'livros': livros})