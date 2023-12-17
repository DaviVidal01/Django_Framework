# --- Render
from django.shortcuts import render, redirect
# --- Forms / BD
from .models import Livro
from .forms import LivroForm, LoginForm
# --- Authenticate
from django.contrib.auth import login, logout
from django.contrib import auth
from django.contrib.auth.models import User
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

    # Verifica se o formulário possui método POST
    if request.method == 'POST':
        login_form = LoginForm(request.POST)

    #Verifica se os dados inseridos no formulário são válidos
    if login_form.is_valid():
        #Pega os dados do formulário de seus específicos names    
        username = login_form['username'].value()
        password = login_form['password'].value()
        #Faz a authenticação do usuário para verificar seus dados
        usuario = auth.authenticate(request, username=username, password=password)

        #Se os dados são coesos, o login é realizado com a authenticação
        if usuario is not None:
            auth.login(request, usuario)
            messages.success(request, 'Foi logado com sucesso!')
            return redirect('lista_livros')
        else:
             messages.error(request, 'Erro ao efetuar login')

    return render(request, 'livro_detalhes.html', {'login_form' : login_form})

def logout_view(request):
    logout(request)
    #Redireciona para a página desejada após o logout
    return redirect('livro_detalhes')