from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.lista_livros, name='lista_livros'),
    path('detalhes/', views.livro_detalhes, name="livro_detalhes"),
    # ----- FORM Livro
    path('adicionar/', views.adicionar_livro, name="adicionar_livro"),
    # ----- Login / Logout Auth
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]