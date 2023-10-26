from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.lista_livros, name='lista_livros'),
    path('detalhes/', views.livro_detalhes, name="livro_detalhes"),
    # ----- FORM Livro
    path('adicionar/', views.adicionar_livro, name="adicionar_livro"),
    # ----- Login / Logout Auth
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]