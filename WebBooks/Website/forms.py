from django import forms

class LivroForm(forms.Form):
    titulo = forms.CharField(label='Título', max_length=100)
    autor = forms.CharField(label='Autor', max_length=100)
    publicação = forms.DateField(label='Data de Publicação')
    paginas = forms.IntegerField(label='Número de Páginas')
    capa = forms.ImageField(label='Capa do Livro')

class LoginForm(forms.Form):
    username = forms.CharField(label="Username", required=True, max_length=100)
    password = forms.CharField(label="Senha", required=True, max_length=100, widget=forms.PasswordInput(attrs={'type':'password'}))
