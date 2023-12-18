from django.test import TestCase, Client
from django.urls import reverse
from .models import Livro
from django.contrib.auth.models import User

class LivroViewsTest(TestCase):
    def setUp(self):
        # Configurações iniciais para os testes
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.livro = Livro.objects.create(
            titulo="Livro de Teste",
            autor="Autor Teste",
            capa="path/to/image.jpg",
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

    def test_adicionar_livro_view(self):
        # Loga o usuário
        self.client.login(username='testuser', password='testpassword')

        # Testa se a view retorna um código de resposta 200 (OK)
        response = self.client.get(reverse('adicionar_livro'))
        self.assertEqual(response.status_code, 200)

        # Testa se o template correto é usado
        self.assertTemplateUsed(response, 'adicionar_livro.html')

        # Adicione mais testes conforme necessário

    def test_editar_livro_view(self):
        # Loga o usuário
        self.client.login(username='testuser', password='testpassword')

        # Testa se a view retorna um código de resposta 200 (OK)
        response = self.client.get(reverse('editar_livro', args=[self.livro.id]))
        self.assertEqual(response.status_code, 200)

        # Testa se o template correto é usado
        self.assertTemplateUsed(response, 'editar_livros.html')

        # Adicione mais testes conforme necessário

    # Adicione mais testes para as outras views conforme necessário

    def test_login_view(self):
        # Testa se a view retorna um código de resposta 200 (OK)
        response = self.client.get(reverse('login_user'))
        self.assertEqual(response.status_code, 200)

        # Testa se o template correto é usado
        self.assertTemplateUsed(response, 'livro_detalhes.html')

        # Adicione mais testes conforme necessário

    def test_logout_view(self):
        # Loga o usuário
        self.client.login(username='testuser', password='testpassword')

        # Testa se a view redireciona corretamente
        response = self.client.get(reverse('logout_user'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('livro_detalhes'))

        # Adicione mais testes conforme necessário

    def test_delete_view(self):
        # Loga o usuário
        self.client.login(username='testuser', password='testpassword')

        # Testa se a view redireciona corretamente após excluir um livro
        response = self.client.get(reverse('delete', args=[self.livro.id]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('lista_livros'))

        # Adicione mais testes conforme necessário

    def test_update_view(self):
        # Loga o usuário
        self.client.login(username='testuser', password='testpassword')

        # Testa se a view redireciona corretamente após editar um livro
        response = self.client.get(reverse('update', args=[self.livro.id]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('lista_livros'))

        # Adicione mais testes conforme necessário