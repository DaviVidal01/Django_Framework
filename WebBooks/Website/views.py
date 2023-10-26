from django.shortcuts import render, redirect
from .models import Livro
from .forms import LivroForm, LoginForm
from django.contrib.auth import login, authenticate, logout
# Create your views here.

def lista_livros(request):
    login_form = LoginForm()
    livros = Livro.objects.all()
    return render(request, 'lista_livros.html', {'livros': livros, 'login_form': login_form})

def livro_detalhes(request):
    login_form = LoginForm()
    livros = Livro.objects.all()
    return render(request, 'livro_detalhes.html', {'livros': livros, 'login_form': login_form})

@login_required
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
    if request.method == 'POST':
        login_form = LoginForm(request, request.POST)
        if login_form.is_valid():
            username_email = login_form.cleaned_data['username_email']
            password = login_form.cleaned_data['password']
            # Verifica se o username_email parece ser um email
            if '@' in username_email :
                user = authenticate(request, email=username_email , password=password)
            else:
                user = authenticate(request, username=username_email , password=password)

            if user is not None:
                login(request, user)
                # Redirecione para a url desejada após o login bem-sucedido
                messages.success(request, 'Login bem-sucedido!')
                return redirect('detalhes')
            else:
                # Usuário ou senha incorretos, você pode adicionar uma mensagem de erro aqui
                messages.error(request, 'Credenciais incorretas. Tente novamente.')
                return render(request, 'livro_detalhes.html')
        else:
            messages.error(request, 'Credenciais incorretas. Tente novamente.')

    return render(request, 'livro_detalhes.html')

def logout_view(request):
    logout(request)
    # Redirecione para a página desejada após o logout.
    return redirect('detalhes')