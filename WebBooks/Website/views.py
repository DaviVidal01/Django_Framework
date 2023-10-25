from django.shortcuts import render, redirect
from .models import Livro
from .forms import LivroForm
from django.contrib.auth import login, authenticate, logout
# Create your views here.

def lista_livros(request):
    livros = Livro.objects.all()
    return render(request, 'lista_livros.html', {'livros': livros})

def livro_detalhes(request):
    livros = Livro.objects.all()
    return render(request, 'livro_detalhes.html', {'livros': livros})

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

def login_view(request):
    if request.method == 'POST':
        username_or_email = request.POST['username_email']
        password = request.POST['password']

        # Verifica se o username_or_email parece ser um email
        if '@' in username_or_email:
            user = authenticate(request, email=username_or_email, password=password)
        else:
            user = authenticate(request, username=username_or_email, password=password)

        if user is not None:
            login(request, user)
            # Redirecione para a url desejada após o login bem-sucedido
            return redirect('detalhes')
        else:
            # Usuário ou senha incorretos, você pode adicionar uma mensagem de erro aqui
            return render(request, 'lista_livros.html', {'error_message': 'Credenciais inválidas'})

    return render(request, 'lista_detalhes.html')

def logout_view(request):
    logout(request)
    # Redirecione para a página desejada após o logout.
    return redirect('detalhes')