from django.shortcuts import render, redirect
from .models import Livro
from .forms import LivroForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def lista_livros(request):
    livros = Livro.objects.all()
    return render(request, 'lista_livros.html', {'livros': livros})

def livro_detalhes(request):
    livros = Livro.objects.all()
    return render(request, 'livro_detalhes.html', {'livros': livros})

@login_required
def adicionar_livro(request):
    if request.method == 'POST':
        livro_form = LivroForm(request.POST, request.FILES)
        if livro_form.is_valid():
            novo_livro = Livro(
                titulo= livro_form.cleaned_data['titulo'],
                autor= livro_form.cleaned_data['autor'],
                publicação= livro_form.cleaned_data['publicação'],
                paginas= livro_form.cleaned_data['paginas'],
                capa = livro_form.cleaned_data['capa']
            )
            novo_livro.save() 

            return redirect('lista_livros')
    else:
        livro_form = LivroForm()

    return render(request, 'adicionar_livro.html', {'livro_form': livro_form})