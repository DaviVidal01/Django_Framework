from django.test import TestCase, Client
from .models import Livro
from django.urls import reverse

# Create your tests here.

# --- Teste Livro
class LivroTest(TestCase):
    def setUp(self):
        # Configurações iniciais para os testes
        Livro.objects.create(titulo="Meu Livro", autor="Autor Teste", publicação="2023-04-10", paginas=200)

    def test_titulo_do_livro(self):
        livro = Livro.objects.get(id=1)
        self.assertEqual(livro.titulo, "Meu Livro")

# --- Teste Views

class LivroViewsTest(TestCase):
    def setUp(self):
        # Configurações iniciais para os testes
        self.client = Client()
        self.livro = Livro.objects.create(
            titulo="Livro de Teste",
            autor="Autor Teste",
            publicação="2023-04-10",
            paginas=200
        )

    def test_lista_livros_view(self):
        # Testa se a view retorna um código de resposta 200 (OK)
        response = self.client.get(reverse('lista_livros'))
        self.assertEqual(response.status_code, 200)

        # Testa se o template correto é usado
        self.assertTemplateUsed(response, 'lista_livros.html')

        # Testa se o livro criado está presente na página
        self.assertContains(response, self.livro.titulo)

        # Adicione mais testes conforme necessário