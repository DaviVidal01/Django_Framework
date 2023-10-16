# 📚 - Tutorial de Desenvolvimento Web com Django

> 👨‍💻 # Este repositório abriga um abrangente tutorial sobre o desenvolvimento web usando o framework Django. Aprenda passo a passo a criar um aplicativo web, desde a configuração inicial até o deploy em um ambiente de produção.

## 📜 Sumário
- [Fase 1: Configuração Inicial e Ambiente de Desenvolvimento](#-fase-1-configuração-inicial-e-ambiente-de-desenvolvimento)
- - [1.1. Instalação do Python e Pip.](#11-instalação-do-python-e-pip)
- - [1.2. Configuração de um ambiente virtual (Virtual Environment).](#12-configuração-de-um-ambiente-virtual-virtual-environment)
- - [1.3. Instalação do Django usando o Pip.](#13-instalação-do-django-usando-o-pip)
- - [1.4. Inicialização de um novo projeto Django.](#14-inicialização-de-um-novo-projeto-django)
- - [1.5. Inicialização de um novo app Django.](#15-inicialização-de-um-novo-app-django)
- - [1.6. Executando o servidor com Runserver](#16-executando-o-servidor-com-runserver)
- [Fase 2: Estrutura de Diretórios e Primeiras Configurações](#-fase-2-estrutura-de-diretórios-e-primeiras-configurações)
- - [2.1. Estrutura de Diretórios do Projeto](#21-estrutura-de-diretórios-do-projeto)
- - [2.2. Configuração do Banco de Dados](#22-configuração-do-banco-de-dados)
- - [2.3. Configuração do Banco de Dados no MySQL Workbench](#23-configuração-do-banco-de-dados-no-mysql-workbench)
- - [2.4. Configuração do Banco de Dados no Django](#24-configuração-do-banco-de-dados-no-django)
- - [2.5. Instalação de Pacotes Python para MySQL no Django](#25-instalação-de-pacotes-python-para-mysql-no-django)
- [Fase 3: Models e Banco de Dados](#-fase-3-models-e-banco-de-dados)
- - [3.1. Criar Modelos](#31-criar-modelos)
- - [3.2. Migrações e Aplicação](#32-migrações-e-aplicação)
- - [3.3. Django Admin](#33-django-admin)
- - [3.4. Criar Superusuário](#34-criar-superusuário)
- [Fase 4: Views e URLs](#-fase-4-views-e-urls)
- - [4.1. Criar Views](#41-criar-views)
- - [4.2. Definir URLs](#42-definir-urls)
- - [4.3. Configurando URLs de Setup](#43-configurando-urls-de-setup)
- - [4.4. Criar um Template](#44-criar-um-template)
- [Fase 5: Templates e Páginas HTML (static, partials, layout, media)](#-fase-5-templates-e-páginas-html-static-partials-layout-media)
- [Fase 6: MVT (Model-View-Template) e Integração]() EM BREVE
- [Fase 7: Administração do Django]() EM BREVE
- [Fase 8: Formulários e Validação]() EM BREVE
- [Fase 9: Autenticação e Autorização]() EM BREVE
- [Fase 10: CRUD (Create, Read, Update, Delete)]() EM BREVE
- [Fase 11: Testes e Depuração]() EM BREVE
- [Fase 12: Deploy (Implantação) em Produção]() EM BREVE

---------------------------------------------------------------

## 📗 Fase 1: Configuração Inicial e Ambiente de Desenvolvimento

### **1.1.** *Instalação do Python e Pip.*

- 🔔 Certifique-se de que o Python e Pip estejam instalados no seu sistema. Você pode verificar isso executando o seguinte comando no seu terminal ou prompt de comando:

```bash
python --version
```

```bash
pip --version
```

> Caso contrário, você pode baixa-los em seus sites e seguirem as instruções de instalação em [Python](https://www.python.org/downloads/) e [Pip](https://pip.pypa.io/en/stable/installation/)
>> Pip (Python Package Installer) geralmente é incluído na instalação do Python mais recente.

### **1.2.** *Configuração de um ambiente virtual (Virtual Environment).*

> 🗃️ # Um ambiente virtual é uma prática recomendada para isolar as dependências do seu projeto. Isso garante que você possa ter várias versões do Django e de outras bibliotecas em diferentes projetos sem conflitos.

##### 1. Abra um terminal ou prompt de comando

##### 2. Navegue até o diretório onde deseja criar seu ambiente virtual.

##### 3. Execute o seguinte comando para criar o ambiente virtual (substitua `nome-do-ambiente` pelo nome que você deseja para o seu ambiente):

- 🖥️ No Windows:
```bash
python -m venv nome-do-ambiente
```

- 💻 No macOS e Linux:
```bash
python3 -m venv nome-do-ambiente
```
##### 4. Para ativar o ambiente virtual, utilize os seguintes comandos no terminal ou prompt de comando:

- 🖥️ No Windows:
```bash
nome-do-ambiente\Scripts\activate
```

- 💻 No macOS e Linux:
```bash
source nome-do-ambiente/bin/activate
```

Agora, você está dentro do ambiente virtual e pode instalar as dependências específicas do projeto, incluindo o Django, quando ativar a venv seu terminal ficará assim:

<img src="README-assets/ex01.png" alt="Exemplo01" />

- 🔩 Lembrando que quando fechar o seu editor e abrir novamente, terá de ativar a venv (ambiente virtual) novamente seguindo a etapa [**1.2.4**](#4-para-ativar-o-ambiente-virtual-utilize-os-seguintes-comandos-no-terminal-ou-prompt-de-comando)

### **1.3.** *Instalação do Django usando o Pip.*

- 🔔 Dentro do ambiente virtual, você pode instalar o Django executando o seguinte comando no terminal ou prompt de comando:

```bash
pip install django
```

Isso instalará a versão mais recente do Django no seu ambiente virtual.

### **1.4.** *Inicialização de um novo projeto Django.*

- 🔔 Agora que o Django está instalado, você pode criar um novo projeto Django com o seguinte comando (substitua **nome-do-projeto** pelo nome que você deseja para o projeto):

- 📌 Recomendo que o nome seja **setup**, dessa forma fica mais fácil para diferenciar a pasta de setup onde serão guardadas as configurações do seu site, depois é só renomear o nome do projeto para **nome-do-projeto** que você desejar.

```bash
django-admin startproject nome-do-projeto
```

ou

```bash
django-admin startproject setup
```

<img src="README-assets/ex02.png" alt="Exemplo02" />

> 👨‍👦 # Assim criará a estrutura inicial do seu projeto Django, incluindo arquivos e diretórios necessários, pode renomear o diretório "pai" do projeto sem alterar o diretório **setup** que estiver dentro dele, normalmente os 2 possuem o mesmo nome, por isso que haverá complicações na hora de navegar.

<img src="README-assets/ex03.png" alt="Exemplo03" />

### **1.5.** *Inicialização de um novo app Django.*

- 🔔 Para criar um novo aplicativo dentro do projeto, execute o seguinte comando no terminal ou prompt de comando dentro do diretório (**nome-do-projeto**) onde é o seu projeto (substitua **nome-do-app** pelo nome do aplicativo):

```bash
cd nome-do-projeto
python manage.py startapp nome-do-app
```

Isso criará a estrutura de diretórios e arquivos para o seu novo aplicativo Django.

<img src="README-assets/ex04.png" alt="Exemplo04" />

### **1.6.** *Executando o servidor com Runserver*
> 📌 # O servidor de desenvolvimento é uma ferramenta que permite que você teste e visualize seu aplicativo enquanto o desenvolve. Lembre-se de que o servidor de desenvolvimento é destinado apenas para uso durante o desenvolvimento e testes.

##### 1. Abra um terminal ou prompt de comando.

##### 2. Navegue até a pasta raiz do seu projeto Django, onde está localizado o arquivo `manage.py`. Use o comando `cd` para acessar a pasta (`WebBooks` é o nome da minha pasta Raiz/Pai do projeto). 
<img src="README-assets/ex14.png" alt="Exemplo14">

##### 3. Agora que você está na pasta do projeto e com o ambiente virtual ativado, você pode iniciar o servidor de desenvolvimento com o seguinte comando:

- 🖥️ No Windows:
```bash
python manage.py runserver
```

- 💻 No macOS e Linux:
```bash
python3 manage.py runserver
```
##### 4. Após executar o comando, o servidor de desenvolvimento começará a ser executado. Você verá mensagens no terminal indicando que o servidor está "exibindo" em um endereço, normalmente em http://127.0.0.1:8000/, é só clicar por cima e entrar no link e você conseguirá observar a página inicial do seu projeto:
<img src="README-assets/ex13.png" alt="Exemplo13">
<img src="README-assets/ex15.png" alt="Exemplo15">

##### 5. Para desligar o Runserver, é só pressionar `Crtl + C` no terminal ou prompt de comando.

---------------------------------------------------------------

## 📗 Fase 2: Estrutura de Diretórios e Primeiras Configurações

### **2.1.** *Estrutura de Diretórios do Projeto*

> 🗂️ # Um projeto Django possui uma estrutura de diretórios organizada. Vamos dar uma olhada nos diretórios e arquivos principais, usaremos os meus exemplos como referência:

- `WebBooks/`: Este é o diretório raiz do seu projeto, no seu caso será o **nome-do-projeto** que você escolheu, além de que pode ser possível renomea-lo sem problemas
- - `setup/`: O diretório interno com o mesmo nome contém as configurações do projeto, caso renomea-lo terá de reconfigurar todos os arquivos internos dele.
- - - `settings.py`: Arquivo de configurações do projeto.
- - - `urls.py`: Arquivo de configurações de URLs.
- - - `wsgi.py`: Arquivo de configuração do servidor WSGI (usado para implantação em produção).
- - `Website/`: O diretório do seu aplicativo.
- - - `__init__.py`: Um arquivo Python vazio que informa ao Python que o diretório deve ser tratado como um pacote.
- - - `admin.py`:  Este arquivo é usado para configurar a administração do aplicativo, permitindo que você gerencie os modelos de dados por meio da interface de administração.
- - - `apps.py`: Arquivo de configuração do aplicativo, onde você pode definir metadados do aplicativo.
- - - `models.py`: Neste arquivo, você define os modelos de dados do aplicativo, que representam as tabelas do banco de dados.
- - - `tests.py`: Este é o local para escrever testes de unidade para o aplicativo.
- - - `views.py`: Neste arquivo, você define as visualizações que controlam a lógica de exibição do aplicativo.
- - - `migrations/`: Este diretório é criado quando você executa migrações e contém os arquivos de migração do aplicativo.
- - - `templates/`: Aqui, você pode criar diretórios e arquivos de modelos HTML usados para renderizar as páginas do aplicativo.
- - - `static/`: Diretório onde você pode armazenar arquivos estáticos, como folhas de estilo CSS, scripts JavaScript e imagens.
- - `manage.py`: Um utilitário de linha de comando para gerenciar seu projeto.

**🔩 - Algumas dessas estruturas iremos criar ao longo do tutorial**

### **2.2.** *Configuração do Banco de Dados*

>🔔 # Nesse tutorial iremos utilizar uma das formas de configurar o banco de dados, que é a utilização do XAMPP, Workbench MySQL e MySQL

##### 1. Instale o XAMPP, MySQL:

- Faça o download e instale o [XAMPP](https://www.apachefriends.org/pt_br/index.html)
- Faça o download e instale o [MySQLclient](https://dev.mysql.com/downloads/installer/) (Marque a opção MySQL Client na hora da instalação)
- Faça o download e instale o [MySQL Workbench](https://dev.mysql.com/downloads/workbench/) (É possível instalar o Workbench apenas com a instalação da etapa acima)

##### 2. Ligando o XAMPP (Apache e MySQL):

- Inicie o XAMPP Control Panel e certifique-se de que o servidor Apache e o servidor MySQL estejam em execução.

<img src="README-assets/ex05.png" alt="Exemplo05">

### **2.3.** *Configuração do Banco de Dados no MySQL Workbench*

- Abra o MySQL Workbench e clica no "+" para criar seu servidor.
<img src="README-assets/ex06.png" alt="Exemplo06">

- Crie um novo servidor MySQL se ainda não tiver um configurado e coloque o nome da "**Connection Name**", se quiser pode colocar uma senha em "**Password**" e clica em "**Ok**"
<img src="README-assets/ex07.png" alt="Exemplo07">

- Anote o nome do banco de dados, o nome de usuário (USERNAME) e a senha (PASSWORD) que você configurou no MySQL Workbench.

- Crie um novo esquema "**schema**" de banco de dados (database) para o seu projeto Django (por exemplo, **'WebBooksBD'**).
<img src="README-assets/ex08.png" alt="Exemplo08">

> É importante que o "**Charset/Collation**" sejam **utf8** e **utf8_unicode_ci** como na imagem, e depois dê **Apply**:
<img src="README-assets/ex09.png" alt="Exemplo09">

>> Depois de concordar tudo e finalizar as confirmações, seu banco será criado:
<img src="README-assets/ex10.png" alt="Exemplo10">

### **2.4.** *Configuração do Banco de Dados no Django*

- Abra o arquivo de configuração do banco de dados no seu projeto Django, que normalmente está localizado em `setup/settings.py`.

- Na seção **INSTALLED_APPS**, você vai inserir o nome do seu app entre os que já foram inseridos, colocando o **'nome-do-app',** dentro da seção como no exemplo:
<img src="README-assets/ex18.png" alt="Exemplo18">

> Caso queira confirmar qual é o nome do seu app, é só entrar no seu app e no arquivo `apps.py`, lá você encontrará esse "**name**", é só copiar e colar.
<img src="README-assets/ex19.png" alt="Exemplo19">

- Na seção **DATABASES**, você pode configurar a conexão com o MySQL Workbench. Substitua as configurações existentes pelas seguintes:

```bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'WebBooksBD',  # Nome do banco de dados que você criou no MySQL Workbench.
        'USER': 'seu_usuario_mysql',  # Nome de usuário do MySQL.
        'PASSWORD': 'sua_senha_mysql',  # Senha do MySQL.
        'HOST': 'localhost',  # Endereço do servidor do MySQL (normalmente 'localhost').
        'PORT': '3306',  # Porta do MySQL (normalmente '3306').
    }
}
```
> Certifique-se de substituir 'seu_usuario_mysql' e 'sua_senha_mysql' pelas credenciais reais do MySQL que você configurou no MySQL Workbench como as do meu:

<img src="README-assets/ex11.png" alt="Exemplo11">

### **2.5.** *Instalação de Pacotes Python para MySQL no Django*
> 🌎 # Aqui iremos instalar os pacotes necessários para o funcionamento do Banco de Dados com Django, vamos instalar os pacotes necessários na Venv
>
> 🚀 # A não ser que você deseja baixar todos esses pacotes e recursos de forma global fora da Venv, você pode sair da venv toda vez que for iniciar o Runserver.
>> **Sair da Venv**: 
>> - Você pode estar fechando e abrindo o editor de codigo que você estiver utilizando, dessa forma a venv fechará também
>> - Caso dessa forma não dê certo, podemos utilizar esses comandos no terminal ou prompt de comando antes de fechar e abrir o editor.
>> 
>> 🖥️ No Windows:
>> ```bash
>> nome-do-ambiente\Scripts\deactivate
>> ```
>> 
>> 💻 No macOS e Linux:
>> ```bash
>> deactivate
>> ```
>
> **Pacotes Necessários**:
> - Para que o Django possa se comunicar com o banco de dados MySQL, você precisa instalar pacotes Python que oferecem suporte ao MySQL. Existem duas opções comuns: `mysql-connector-python` e `mysqlclient`.
>
> ```bash
> pip install mysql-connector-python
> ```
> ```bash
> pip install mysqlclient
> ```
>
> **Exemplo sem a Venv:**

<img src="README-assets/ex12.png" alt="Exemplo12">

> 🛡️ - Depois ative novamente a Venv que você desativou usando os comandos que já foram ensinados para dar continuidade as configurações do seu projeto.

---------------------------------------------------------------

## 📗 Fase 3: Models e Banco de Dados

> 🔔 # Nesta fase, você criará modelos para representar dados em seu aplicativo Django e entenderá como o Django ORM (Object-Relational Mapping) funciona para mapear esses modelos para tabelas no banco de dados.

### **3.1.** *Criar Modelos*

- Modelos são classes que definem a estrutura dos dados que você deseja armazenar em seu banco de dados. Vamos criar um modelo simples como exemplo. Suponha que você esteja criando um aplicativo de gerenciamento de livros. Aqui está um exemplo de modelo de livro:

##### 1. Abra o arquivo `models.py` no diretório do seu aplicativo (por exemplo, `Website/models.py`).
<img src="README-assets/ex16.png" alt="Exemplo16">

##### 2. Crie uma classe para o modelo de livro:
```bash
from django.db import models

class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    publicação = models.DateField()
    paginas = models.IntegerField()
```
> 🔔 - Neste exemplo, criamos um modelo de livro com campos como título, autor, data de publicação e número de páginas. Você pode personalizar os campos de acordo com suas necessidades.

### **3.2.** *Migrações e Aplicação*

- Agora que você criou o modelo, é hora de criar uma migração para aplicá-lo ao banco de dados.

##### 1. No terminal, dentro do diretório raiz/pai do projeto, execute o seguinte comando para criar uma migração:
```bash
python manage.py makemigrations
```
##### 2. Em seguida, execute o comando para aplicar a migração:
```bash
python manage.py migrate
```
<img src="README-assets/ex20.png" alt="Exemplo20">

### **3.3.** *Django Admin*

- O Django oferece um painel de administração prontamente disponível para gerenciar os dados do banco de dados. Vamos habilitá-lo.

##### 1. Abra o arquivo `admin.py` no diretório do seu aplicativo (por exemplo, `Website/admin.py`).
<img src="README-assets/ex17.png" alt="Exemplo17">

##### 2. Registre o modelo de livro no painel de administração:
```bash
from django.contrib import admin
from .models import Livro

admin.site.register(Livro)
```

> - **from .models import Livro:** Retira de dentro do arquivo `models.py` a class chamada `Livro`.
> - **admin.site.register(Livro):** Indica que no painel de Administrador do Django será possível registrar dados na tabela chamada `Livro`.

### **3.4.** *Criar Superusuário*

- Para acessar o painel de administração, você precisará criar um superusuário.

- No terminal, dentro do diretório do projeto, execute o seguinte comando e siga as instruções para criar um superusuário, e depois preencha os parâmetros com nome e senha que você não esquecerá, se preferir pode usar como no exemplo:

<img src="README-assets/ex21.png" alt="Exemplo21">

> 🔩 - O Password é invisível por questões de segurança, o Email pode ser aleatório ou o seu oficial, as informações colocadas no exemplo são:
> - Username: admin
> - Email: admin@admin.com
> - Password: 1234
> - Password (again): 1234
> - Confirmação se vou usar senha fraca: y

- Agora quando você fazer o comando do **Runserver** que já foi ensinado na etapa [**1.6.3**](#3-agora-que-você-está-na-pasta-do-projeto-e-com-o-ambiente-virtual-ativado-você-pode-iniciar-o-servidor-de-desenvolvimento-com-o-seguinte-comando), vá na URL do seu navegador e adiciona `/admin` e faça o login da sua conta que você criou aqui no Django.

<img src="README-assets/ex22.png" alt="Exemplo22">

<img src="README-assets/ex23.png" alt="Exemplo23">

<img src="README-assets/ex24.png" alt="Exemplo24">

> 🎛️ # Nesse painel você consegue ter acesso para inserir informações, remover, editar e ler dados inseridos no seu banco de dados, esse ambiente não é recomendável que seja acessado por qualquer usuário, até mesmo para funcionários, é um ambiente de trabalho apenas do ADM do Banco de Dados ou usuários com privilégios elevados.
---------------------------------------------------------------

## 📗 Fase 4: Views e URLs

### **4.1.** *Criar Views*

- Views são funções ou classes que processam solicitações do navegador e retornam respostas. Vamos criar uma view simples que exibe uma lista de livros.

##### 1. Abra o arquivo `views.py` no diretório do seu aplicativo (por exemplo, `Website/views.py`).

<img src="README-assets/ex25.png" alt="Exemplo25">

##### 2. Crie uma view:
```bash
from django.shortcuts import render
from .models import Livro

def lista_livros(request):
    livros = Livro.objects.all()
    return render(request, 'lista_livros.html', {'livros': livros})
```

> Nesta view, estamos obtendo todos os objetos de livro do banco de dados e passando-os para um template chamado *lista_livros.html*.
> - **livros = Livro.objects.all():** Pega todos os `objects` de models chamado `Livro` e passa-os para dentro da variável `livros`.
> - **render(request, 'lista_livros.html'):** Ele renderizará usando o `request`, o template (site) chamado `lista_livros.html` de dentro da pasta `templates` *(OBS: vamos criar a pasta ainda)*.
> - **{'livros' : livros}:** Ele criará um dicionário chamado `livros` e pegará a variável `livros` e receber todas as informações guardadas dentro da variável.

### **4.2.** *Definir URLs*

> 🔔 # As URLs mapeiam solicitações para views. Vamos definir uma URL que chama a view `lista_livros`.

##### 1. Crie um arquivo chamado `urls.py` no diretório do seu aplicativo (por exemplo, `Website/urls.py`).

<img src="README-assets/ex36.png" alt="Exemplo36">

##### 2. Defina a URL dentro do arquivo `urls.py` no diretório do seu aplicativo:

```bash
from django.urls import path
from . import views

urlpatterns = [
    path('livros/', views.lista_livros, name='lista_livros'),
]
```

> Agora, quando os usuários acessarem `/livros/` em seu site, a view *lista_livros* será chamada.
> - **from . import views:** Importa da pasta atual (Website) tudo do arquivo views.py (Class, Funções, Métodos, etc.)
> - **path('livros/', views.lista_livros, name='lista_livros'):** Para acessar a `views.lista_livros` é necessário que o usuário esteja na página da URL `livros/`, o nome dessa path é nomeada de `lista_livros`
>>📌 *OBS:* A colocação de "," dentro do `urlpatterns` permite que possa ser criada várias `path` de uma vez, então é possível a criação de várias views e URLs para essas views em seu aplicativo.

### **4.3.** *Configurando URLs de Setup*

> 🔔 # Para que o setup do seu projeto reconheça que as configurações feitas nas URLs de dentro do seu aplicativo (Website) são oficiais, é necessário interligar uma ponte de acesso entre eles utilizando o `include`

- Navegue até o setup do seu diretório Raiz/Pai, procure pelo arquivo chamado `urls.py` e faça as devidas interligações:

```bash
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Website.urls'))

]
```
- Como no exemplo:

<img src="README-assets/ex31.png" alt="Exemplo31">

> - **path('', include('Website.urls')):** Ele faz um path dizendo que naturalmente todas as urls do aplicativo chamado `Website` localizados dentro do arquivo `urls` sejam acrescentadas/incluidas.

### **4.4.** *Criar um Template*

> 🔔 # Um template é um arquivo HTML que define como os dados são apresentados. Vamos criar um template para exibir a lista de livros.

##### 1. Crie uma pasta chamada `templates` no diretório do seu aplicativo (por exemplo, `Website/templates`).

<img src="README-assets/ex26.png" alt="Exemplo26">

##### 2. Dentro da pasta templates, crie um arquivo chamado `lista_livros.html` (por exemplo, `Website/templates/lista_livros.html`)

<img src="README-assets/ex27.png" alt="Exemplo27">

##### 3. No arquivo `lista_livros.html`, você pode usar os dados passados pela view para criar a página da web:

```bash
<!DOCTYPE html>
<html>
    <head>
        <title>Lista de Livros</title>
    </head>
    <body>
        <h1>Lista de Livros</h1>
        <ul>
            {% for livro in livros %}
            <li>{{ livro.titulo }} por {{ livro.autor }}</li>
            {% endfor %}
        </ul>
    </body>
</html>
```

> - **{% for livro in livros %}:** Aqui ele cria um "x" com o nome de `livro`, esse x vai passar por todos os itens que haver no "nome-representativo" chamado `livros` que interliga na views a variável chamada `livros` que você criou na etapa [**4.1.2**](#2-crie-uma-view)
>> 📌 *OBS:* Esse `{livros : livros}` que está na imagem de exemplo é igual a `{nome-representativo : variável}`, pois criamos um "nome-representativo" para referenciar no HTML a "variável" informada na views, que é a variável `livros = Livro.objects.all()`.

<img src="README-assets/ex37.png" alt="Exemplo37">

> - **{{ livro.titulo }}:** A lógica é parecida como as lógicas abordadas em programações da linguagem C, pegando um "x" que irá receber todos os valores de `titulo` 1 por vez e apresentarem todas 1 por vez no HTML. Isso é a mesma coisa com o `{{ livro.autor }}` também, é a mesma lógica de programação.
> - **{% endfor %}:** O **FOR** só irá acabar quando TODOS os itens de cada campo informado dentro dele (por exemplo, `{{ livro.titulo }}`) forem apresentados.

##### 4. Testar a View

- Agora, você pode iniciar o servidor de desenvolvimento do Django e testar sua view, utilize runserver para testar o seu site como foi ensinado no [**1.6.3**](#3-agora-que-você-está-na-pasta-do-projeto-e-com-o-ambiente-virtual-ativado-você-pode-iniciar-o-servidor-de-desenvolvimento-com-o-seguinte-comando)

✔️ ▶ Lembre-se de ativar a sua Venv que foi ensinado no [**1.2.4**](#4-para-ativar-o-ambiente-virtual-utilize-os-seguintes-comandos-no-terminal-ou-prompt-de-comando)

🚫 ***ERROR - Caso você não ative:***

<img src="README-assets/ex29.png" alt="Exemplo29">

✔️ ▶ Lembre-se de deixar o seu Banco de Dados MySQL ligado (XAMPP) como foi ensinado no [**2.2.2**](#2-ligando-o-xampp-apache-e-mysql)

🚫 ***ERROR - Caso você não ligue:***

<img src="README-assets/ex28.png" alt="Exemplo28">

✔️ ▶ Lembre-se de digitar a URL corretamente como imagem mostrada no [**3.4**](#34-criar-superusuário)

🚫 ***ERROR - Caso você não digite:***

<img src="README-assets/ex32.png" alt="Exemplo32">

> 🗂️ - *OBS:* A página descreve quais URLs estão disponíveis

- Depois de tudo estiver em ordem, você poderá acessar a página com o Link que aparecerá quando você realizar o comando de Runserver.

<img src="README-assets/ex30.png" alt="Exemplo30">

<img src="README-assets/ex33.png" alt="Exemplo33">

- Os livros não foram adicionados ainda pelo **FOR** no HTML, pois não há nenhum livro registrado no seu banco.

##### EXTRA. Tornar a página como principal (index), sem a necessidade de digitar `livros/` toda hora, para que ela possa aparecer sem essa necessidade.

> 🎛️ # Para tornar uma das páginas do seu app como principal (index), é necessário que você reconfigure a URL dessa página, é bem simples:

<img src="README-assets/ex34.png" alt="Exemplo34">

- Dessa forma o site assim que iniciar o servidor, irá te levar até a página diretamente sem a digitação na url.

<img src="README-assets/ex35.png" alt="Exemplo35">

---------------------------------------------------------------

## 📗 Fase 5: Templates e Páginas HTML (static, partials, layout, media)

> 🔔 # Nesta fase, você aprenderá a criar templates para renderizar páginas HTML e tornar sua aplicação mais dinâmica. Além disso, veremos como lidar com arquivos estáticos, criar templates parciais e layouts, e como gerenciar arquivos de mídia.

### **5.1.** *Criar Templates HTML*

- Os templates HTML são usados para renderizar páginas da web com dados dinâmicos. Vamos criar um template simples para exibir detalhes de um livro.

##### 1. Crie um arquivo HTML chamado `livro_detalhes.html` em sua pasta de templates do aplicativo (por exemplo, `Website/templates/livros_detalhes.html`).

<img src="README-assets/ex38.png" alt="Exemplo38">

- Depois de criar o HTML (template), você terá de vincula-lo a uma View ou URLs, volte as etapas anteriores para rever como criar uma View e URL na [Fase 4: Views e URLs](#-fase-4-views-e-urls).

<img src="README-assets/ex39.png" alt="Exemplo39">

<img src="README-assets/ex40.png" alt="Exemplo40">

##### 2. Adicione o seguinte conteúdo ao `livro_detalhes.html` como exemplo:

```bash
<!DOCTYPE html>
<html>
    <head>
        <!--CSS-->
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css">
        <link rel="stylesheet" href="style.css">
        <!--Titulo-->
        <title>Detalhes do Livro</title>
    </head>
    <body>
        <!--Header-->
        <header class="d-flex justify-content-center py-3">
            <ul class="nav nav-pills">
              <li class="nav-item"><a href="../" class="nav-link" aria-current="page">Listar</a></li>
              <li class="nav-item"><a href="../detalhes" class="nav-link">Detalhes</a></li>
            </ul>
        </header>
        <!--Main-->
        <main>
            <img src="Exemplo-img.jpg" alt="">
            {% for livro in livros %}
            <h1 class="border-bottom border-danger">{{ livro.titulo }}</h1>
            <p>Autor: {{ livro.autor }}</p>
            <p>Data de Publicação: {{ livro.publicação }}</p>
            <p>Número de Páginas: {{ livro.paginas }}</p>
            {% endfor %}
        </main>
        <!--Footer-->
        <footer class="d-flex flex-wrap justify-content-between align-items-center py-3 my-4 border-top">
            <div class="col-md-4 d-flex align-items-center">
              <a href="https://github.com/DaviVidal01">
                <img width="30px" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/github/github-original.svg"/>
              </a>
              <span class="mb-3 mb-md-0 text-body-secondary">© 2023 WebBooks, copyright.</span>
            </div>
        
            <ul class="nav col-md-4 justify-content-end list-unstyled d-flex">
              <li class="ms-3"><a class="text-body-secondary" href="https://github.com/DaviVidal01"><img width="30px" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/github/github-original.svg"/></a></li>
              <li class="ms-3"><a href="https://github.com/DaviVidal01/"><img src="https://camo.githubusercontent.com/cf57d31040e997c7ab2d909aedf085957c88cffe5f6e24b5a7d4d317b65d3689/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f666f6c6c6f776572732f44617669566964616c30313f6c6162656c3d666f6c6c6f77267374796c653d736f6369616c" data-canonical-src="https://img.shields.io/github/followers/DaviVidal01?label=follow&amp;style=social" style="max-width: 100%;"></a></li>
            </ul>
          </footer>
        <!--Scripts-->
        <script src="bootstrap.bundle.min.js"></script>
    </body>
</html>
```

>📌 - É bem grande mesmo, pois estamos simulando um site completo agora, se você observar, terá comentários (<!--Comentários-->) marcando a posição de cada parte do HTML, por exemplo (CSS, Scripts, Header, Main, Footer, etc.). Se estiver trabalhando em equipe ou sozinho, é uma ótima forma de organizar o seu código.

- Mas ainda há coisas faltando nesse template, colocamos exatamente as informações, mas o site ainda não aparece todas as informações que pedi, como CSS, JS ou Imagem.

<img src="README-assets/ex41.png" alt="Exemplo41">

> 💻 - *OBS:* Não iniciei o server para mostrar o Site, apenas abri o HTML, por isso aparece os "{{ livro.titulo }}", pois apenas abrir um arquivo HTML não irá funcionar o banco.

### **5.2.** *Configurando Arquivos Estáticos*

- Agora você precisa configurar seu aplicativo para servir arquivos estáticos corretamente durante o desenvolvimento e implantação.

##### 1. Abra o arquivo de configuração `settings.py`, como por exemplo (`WebBooks/setup/settings.py`) e coloque o codigo `import os` no topo.

<img src="README-assets/ex46.png" alt="Exemplo46">

##### 2. Vá até a seção **TEMPLATES** e faça as seguintes alterações como no exemplo:

<img src="README-assets/ex47.png" alt="Exemplo47">

>🔩 - Isso mostrará ao Django que o seu TEMPLATES está localizado no seu app em um arquivo chamado `templates`

##### 3. Vá até a seção **STATIC_URL** e faça as seguintes alterações como no exemplo:

<img src="README-assets/ex49.png" alt="Exemplo49">

>🔩 - Isso mostrará ao Django que o seu comando é `static`, que localiza a pasta através da URL `static/`, onde os arquivos bases estão localizados em `setup/static`

<img src="README-assets/ex48.png" alt="Exemplo48">

- Se já tiver arquivos dentro da pasta Static, ele vai perguntar se deseja copia-los, ele logo enviará a cópia para onde os arquivos static que você redirecionou na `settings.py`

### **5.3.** *Arquivos Estáticos (CSS, JS, Imagens)*

- Os arquivos estáticos, como CSS, JavaScript e imagens, podem ser usados para estilizar e enriquecer seu site. Vamos configurar os arquivos estáticos.

##### 1. Crie uma pasta chamada `static` no diretório setup do seu projeto (por exemplo, `WebBooks/setup/static`)

<img src="README-assets/ex42.png" alt="Exemplo42">

##### 2. Dentro dela crie subpastas para armazenar arquivos estáticos como `css`, `js` e `img` logo depois adicione e carregue todos os arquivos CSS, JavaScript e Imagens nessas pastas conforme necessário.

<img src="README-assets/ex43.png" alt="Exemplo43">

##### 3. No HTML onde está sendo utilizado esses recursos vão ser atualizado os códigos para Imagens e Links (Hrefs, Src, Script, etc.)

> - Coloque o código `{% load static %}` no topo do HTML, pois ele serve para recarregar todos os componentes de dentro da pasta Static.
> - Modifique os codigos que contém Href, Src e Script que tiverem redirecionamento por diretórios como `src= 'css/style.css'`.
> - Na modificação você colocará o código `{% static 'seu-redirecionamento' %}`, por favor, respeite os espaços e a forma que é escrita o código, senão falhará.

- Exemplo:
**Antes -**
<img src="README-assets/ex44.png" alt="Exemplo44">

**Depois -**
<img src="README-assets/ex45.png" alt="Exemplo45">

> 🗂️ - *OBS:* Não há necessidade de fazer isso com Links "http" como no exemplo, eles não são links de pasta. Agora modifique todos os códigos que contem esses recursos de Href, Src ou Script para que seu site funcione corretamente.

##### 4. Abrir o terminal ou prompt de comando e navegar até o diretório Raiz/Pai e realizar o comando:

```bash
python ./manage.py collectstatic
```

### **5.4.** *Uso de Modelos Parciais (Partial Templates):*

