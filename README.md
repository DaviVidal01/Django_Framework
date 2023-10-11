# Tutorial de Desenvolvimento Web com Django
> 👨‍💻 # Este repositório abriga um abrangente tutorial sobre o desenvolvimento web usando o framework Django. Aprenda passo a passo a criar um aplicativo web, desde a configuração inicial até o deploy em um ambiente de produção.

## 📗 Fase 1: Configuração Inicial e Ambiente de Desenvolvimento

#### **1.1.** *Instalação do Python e Pip.*
- 🔔 Certifique-se de que o Python e Pip estejam instalados no seu sistema. Você pode verificar isso executando o seguinte comando no seu terminal ou prompt de comando:

`python --version`

`pip --version`

> Caso contrário, você pode baixa-los em seus sites e seguirem as instruções de instalação em [Python](https://www.python.org/downloads/) e [Pip](https://pip.pypa.io/en/stable/installation/)
>> Pip (Python Package Installer) geralmente é incluído na instalação do Python mais recente.

#### **1.2.** *Configuração de um ambiente virtual (Virtual Environment).*
> 🗃️ # Um ambiente virtual é uma prática recomendada para isolar as dependências do seu projeto. Isso garante que você possa ter várias versões do Django e de outras bibliotecas em diferentes projetos sem conflitos.

1. Abra um terminal ou prompt de comando
2. Navegue até o diretório onde deseja criar seu ambiente virtual.
3. Execute o seguinte comando para criar o ambiente virtual (substitua **nome-do-ambiente** pelo nome que você deseja para o seu ambiente):

- 🖥️ No Windows:
`python -m venv nome-do-ambiente`

- 💻 No macOS e Linux:
`python3 -m venv nome-do-ambiente`
4. Para ativar o ambiente virtual, utilize os seguintes comandos no terminal ou prompt de comando:

- 🖥️ No Windows:
`nome-do-ambiente\Scripts\activate`

- 💻 No macOS e Linux:
`source nome-do-ambiente/bin/activate`

Agora, você está dentro do ambiente virtual e pode instalar as dependências específicas do projeto, incluindo o Django.

- 🔩 Lembrando que quando fechar o seu editor, terá de ativar a venv (ambiente) novamente seguindo a etapa 1.2.4

#### **1.3.** *Instalação do Django usando o Pip.*
- 🔔 Dentro do ambiente virtual, você pode instalar o Django executando o seguinte comando no terminal ou prompt de comando:

`pip install django`

Isso instalará a versão mais recente do Django no seu ambiente virtual.

#### **1.4.** *Inicialização de um novo projeto Django.*
- 🔔 Agora que o Django está instalado, você pode criar um novo projeto Django com o seguinte comando (substitua **nome-do-projeto** pelo nome que você deseja para o projeto):

- 📌 Recomendo que o nome seja **setup**, dessa forma fica mais fácil para diferenciar a pasta de setup onde serão guardadas as configurações do seu site, depois é só renomear o nome do projeto para **nome-do-projeto** que você desejar.

`django-admin startproject nome-do-projeto`

ou

`django-admin startproject setup`

> 👨‍👦 # Assim criará a estrutura inicial do seu projeto Django, incluindo arquivos e diretórios necessários, pode renomear o diretório "pai" do projeto sem alterar o diretório **setup** que estiver dentro dele, normalmente os 2 possuem o mesmo nome, por isso que haverá complicações na hora de navegar.

#### **1.5.** *Inicialização de um novo app Django.*

- 🔔 Para criar um novo aplicativo dentro do projeto, execute o seguinte comando no terminal ou prompt de comando (substitua **nome-do-app** pelo nome do aplicativo):

`cd <nome-do-projeto>
python manage.py startapp <nome-do-app>`

Isso criará a estrutura de diretórios e arquivos para o seu novo aplicativo Django.

---------------------------------------------------------------