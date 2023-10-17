from django.contrib import admin
from .models import Livro

# Register your models here.
@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'publicação')
    list_filter = ('autor', 'publicação')
    search_fields = ('titulo', 'autor')
    fieldsets = [
        ('Informações Básicas', {'fields': ['titulo', 'autor', 'publicação']}),
        ('Detalhes Adicionais', {'fields': ['paginas', 'capa']}),
    ]