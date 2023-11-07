from django.urls import path
from . import views


urlpatterns = [
    path('', views.lista_livros, name='lista_livros'),
    path('detalhes/', views.livro_detalhes, name="livro_detalhes"),
    # ----- FORM Livro
    path('adicionar/', views.adicionar_livro, name="adicionar_livro"),
    # ----- Login / Logout Auth
    path('login_user/', views.login_view, name='login_user'),
    path('logout_user/', views.logout_view, name='logout_user'),
]