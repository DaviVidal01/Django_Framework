# Tutorial de Desenvolvimento Web com Django

> 👨‍💻 # Este repositório abriga um abrangente tutorial sobre o desenvolvimento web usando o framework Django. Aprenda passo a passo a criar um aplicativo web, desde a configuração inicial até o deploy em um ambiente de produção.

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

- 🔩 Lembrando que quando fechar o seu editor e abrir novamente, terá de ativar a venv (ambiente virtual) novamente seguindo a etapa 1.2.4

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
> 🌎 # Aqui iremos instalar os pacotes necessários para o funcionamento do Banco de Dados com Django, vamos fazer esses comandos de forma globalmente, assim você não precisará usar esses comandos denovo em seu sistema.
>
> 🚀 # A não ser que você deseja baixar todos esses pacotes e recursos em uma Venv, mas vamos seguir o tutorial com a instalação global.
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

> 🛡️ - Depois ative novamente a Venv que você desativou usando os comandos que já foram ensinados.

---------------------------------------------------------------