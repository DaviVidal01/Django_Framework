from django import forms
from django.contrib.auth.forms import AuthenticationForm

class LivroForm(forms.Form):
    titulo = forms.CharField(label='Título', max_length=100)
    autor = forms.CharField(label='Autor', max_length=100)
    publicação = forms.DateField(label='Data de Publicação')
    paginas = forms.IntegerField(label='Número de Páginas')
    capa = forms.ImageField(label='Capa do Livro')

class LoginForm(AuthenticationForm):
    username_email = forms.CharField(label="Nome / Email")
    password = forms.CharField(label="Senha", widget=forms.PasswordInput)
