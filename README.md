# Brascode
Sistema de gerenciamento de times de futebol, jogadores, partidas e torneios, desenvolvido com o framework Django. Esta aplicação oferece uma plataforma completa para acompanhar e administrar informações relacionadas ao mundo do futebol, desde detalhes de times e jogadores até o registro de partidas e torneios.

## Funcionalidades Principais
- **Cadastro de Times:** Crie e gerencie informações detalhadas sobre os times de futebol, incluindo nome, abreviação, data de fundação, país de origem, escudo, cores, técnico e muito mais.
- **Registo de Jogadores:** Cadastre jogadores com informações como nome, idade, nacionalidade, data de nascimento, posição, preferência de pé, número da camisa, altura e peso. Associe cada jogador a um time.
- **Registro de Partidas e Gols:** Registre as partidas de futebol, incluindo data de início, data de término, estádio, times envolvidos e torneio correspondente. Registre gols em cada partida, indicando o jogador que marcou, o tempo do gol e se foi contra.
- **Gestão de Torneios:** Crie e gerencie torneios de futebol, vinculando-os aos jogos correspondentes. Acompanhe as classificações e os resultados dos torneios.
- **Estatísticas de Times:** Visualize as estatísticas de times, como gols marcados, gols sofridos, vitórias, derrotas, empates e pontuação com base nos resultados das partidas.
- **Controle de Pontuação:** Visualize a quantidade de pontos das equipes com base nas vitórias, empates e pontuações dos torneios.

## Como Instalar e Executar
Siga os passos abaixo para configurar e rodar o Projeto Brascode em sua máquina local:

### Instalação dos Requisitos 

1. **Python**: Você pode baixar o Python do site oficial [aqui](https://www.python.org/downloads/).
2. **PyCharm**: Baixe e instale o PyCharm da JetBrains [aqui](https://www.jetbrains.com/pycharm/download/).
3. **Git Bash**: O Git Bash pode ser baixado e instalado a partir deste [link](https://gitforwindows.org/).
4. **MySQL**: Você pode baixar o MySQL [aqui](https://dev.mysql.com/downloads/installer/).

### Passo 1: Clonar o Repositório
1. Abra um terminal ou prompt de comando.
2. Navegue para a pasta onde você deseja clonar o repositório do projeto:
   ```sh
   cd /caminho/para/a/sua/pasta/
3. Clone o repositório do projeto do Git (substitua URL_DO_REPOSITORIO pelo URL do seu repositório):
   ```sh
   git clone URL_DO_REPOSITORIO
   
### Passo 2: Configurar o Ambiente Virtual
1. Certifique-se de ter o Python instalado. Você pode verificar a versão do Python com o comando (Utilizo a versão 3.10):
   ```sh
   python --version
2. Se você ainda não tiver, instale o virtualenv:
   ```sh
   pip install virtualenv
4. Crie um ambiente virtual na pasta do projeto:
   ```sh
   virtualenv venv
5. Ative o ambiente virtual:
   ```sh
   venv\Scripts\activate
   
### Passo 3: Instalar Dependências
1. Navegue para a pasta raiz do projeto onde está localizado o arquivo requirements.txt:
   ```sh
   cd /caminho/para/a/pasta/do/projeto/
2. Instale as dependências do projeto:
   ```sh
   pip install -r requirements.txt
   
### Passo 4: Configurar o Banco de Dados
1. Certifique-se de que você tenha um banco de dados configurado no arquivo de configuração do Django (normalmente em settings.py). O banco de dados utilizado é o MySQL.
2. Execute as migrações para criar as tabelas do banco de dados:
   ```sh
   python manage.py migrate
   
### Passo 5: Executar o Servidor de Desenvolvimento
1. Inicie o servidor de desenvolvimento do Django:
   ```sh
   python manage.py runserver
2. O servidor de desenvolvimento será executado na porta padrão 8000. Você pode acessar o projeto no navegador em http://localhost:8000/.

### Passo 6: Usar o Projeto
Agora, seu projeto Django está em execução localmente. Você pode acessá-lo no navegador e começar a explorar suas funcionalidades. Certifique-se de seguir a documentação específica do seu projeto para entender como usá-lo e personalizá-lo de acordo com suas necessidades.

Lembre-se de adaptar os comandos e configurações de acordo com as peculiaridades da sua máquina. Essas instruções são um guia geral para instalar e rodar projetos Django.
