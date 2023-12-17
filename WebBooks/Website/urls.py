from django.urls import path
from . import views


urlpatterns = [
    path('', views.lista_livros, name='lista_livros'),
    path('detalhes/', views.livro_detalhes, name="livro_detalhes"),
    # ----- CRUD Livro
    path('adicionar/', views.adicionar_livro, name="adicionar_livro"),
    path('delete/<int:id>', views.delete, name="delete"),
    path('update/<int:id>', views.update, name="update"),
    # ----- Login / Logout Auth
    path('login_user/', views.login_view, name='login_user'),
    path('logout_user/', views.logout_view, name='logout_user'),
]