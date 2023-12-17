from django import forms
from .models import Livro

class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = '__all__'

class LoginForm(forms.Form):
    username = forms.CharField(label="Username", required=True, max_length=100)
    password = forms.CharField(label="Senha", required=True, max_length=100,widget=forms.PasswordInput(attrs={"type":"password"}))
