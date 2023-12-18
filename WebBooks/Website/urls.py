from django.urls import path
from . import views
if DEBUG:
    from django.conf import settings
    import debug_toolbar

urlpatterns = [
    path('__debug__/', include(debug_toolbar.urls)),
    path('', views.lista_livros, name='lista_livros'),
    path('detalhes/', views.livro_detalhes, name="livro_detalhes"),
    # ----- CRUD Livro
    path('adicionar/', views.adicionar_livro, name="adicionar_livro"),
    path('editar_livro/<int:id>', views.editar_livro, name="editar_livro"),
    path('delete/<int:id>', views.delete, name="delete"),
    path('update/<int:id>', views.update, name="update"),
    # ----- Login / Logout Auth
    path('login_user/', views.login_view, name='login_user'),
    path('logout_user/', views.logout_view, name='logout_user'),
]

# Configuração para a barra de ferramentas
settings.INSTALLED_APPS += ['debug_toolbar']
settings.MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware']
settings.DEBUG_TOOLBAR_CONFIG = {'SHOW_TOOLBAR_CALLBACK': lambda request: DEBUG}