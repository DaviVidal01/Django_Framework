from .models import Livro
from .forms import LivroForm, LoginForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
# Create your views here.

def lista_livros(request):
    login_form = LoginForm()
    livros = Livro.objects.all()
    return render(request, 'lista_livros.html', {'livros': livros, 'login_form': login_form})

def livro_detalhes(request):
    login_form = LoginForm()
    livros = Livro.objects.all()
    return render(request, 'livro_detalhes.html', {'livros': livros, 'login_form': login_form})

def adicionar_livro(request):
    login_form = LoginForm()
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
        

    return render(request, 'adicionar_livro.html', {'livro_form': livro_form, 'login_form': login_form})

def login_view(request):
    login_form = LoginForm()

    if request.method == 'POST':
        login_form = LoginForm(request.POST)

    if login_form.is_valid():
        username_or_email = login_form['username_email'].value()
        password = login_form['password'].value()
        # Verifica se o username_or_email parece ser um email
        if '@' in username_or_email:
            usuario = auth.authenticate(request, email=username_or_email, password=password)
        else:
            usuario = auth.authenticate(request, username=username_or_email, password=password)

        if usuario is not None:
            auth.login(request, usuario)
            messages.success(request, 'Foi logado com sucesso!')                # Redirecione para a url desejada após o login bem-sucedido
            return redirect('lista_livros')
        else:
            # Usuário ou senha incorretos, você pode    adicionar uma mensagem de erro aqui                messages.error(request, 'Erro ao efetuar login')
            return render(request, 'livro_detalhes.html')

    return render(request, 'livro_detalhes.html', {'login_form' : login_form})

def logout_view(request):
    logout(request)
    # Redirecione para a página desejada após o logout.
    return redirect('detalhes')