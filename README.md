# Scraping de Preços de Produtos KaBuM! e Envio para o Telegram

<div align="center">
  <img src="assets/banner-repositorio-webscraping-playwright-product-kabum-e-commerce-bot-telegram.png" />
</div>


## Índice

1. [Tecnologias Utilizadas](#1-tecnologias-utilizadas)
2. [Pré-requisitos](#2-pré-requisitos)
3. [Instalação e Configuração](#3-instalação-e-configuração)
    1. [Criar o Bot no Telegram](#31-criar-o-bot-no-telegram)
    2. [Instalar as Dependências](#32-instalar-as-dependências)
    3. [Instalar Navegadores do Playwright](#33-instalar-navegadores-do-playwright)
    4. [Configurando o dotenv](#34-configurando-o-dotenv)
4. [Executando o Script](#4-executando-o-script)
5. [Configuração do GitHub Actions](#5-configuração-do-github-actions)
6. [Resultado](#6-resultado)
7. [Contribuindo](#6-contribuindo)

## 1. Tecnologias Utilizadas

- **Playwright**: Framework para automação de navegador, utilizado para realizar o scraping.
- **python-telegram-bot**: Biblioteca para interação com a API do Telegram e envio de mensagens.
- **GitHub Actions**: Ferramenta para automação de workflows, usada para agendar a execução diária do scraping.

## 2. Pré-requisitos

- Python 3.7 ou superior
- Conta no Telegram e criação de um Bot
- Acesso ao repositório GitHub para configurar a automação

## 3. Instalação e Configuração

### 3.1 Criar o Bot no Telegram

Para interagir com o **Telegram Bot**, siga os passos abaixo:

1. Abra o Telegram e procure por **@BotFather**.
2. Envie o comando `/newbot` para o **BotFather**.
3. Siga as instruções para criar o bot e obtenha o **Token do Bot**.
4. Adicione o bot ao seu canal e obtenha o **ID do Canal**. Você pode usar o **BotFather** para encontrar o ID do canal.

### 3.2 Instalar as Dependências

Instale as dependências necessárias utilizando o `pip`:

```bash
pip install -r requirements.txt
```

### 3.3 Instalar Navegadores do Playwright

O Playwright requer que você instale os navegadores para o scraping. Execute o seguinte comando:

```bash
python -m playwright install
```

### 3.4 Configurando o dotenv

O arquivo .env será utilizado para armazenar as variáveis de ambiente, como o Token do Bot e o ID do Canal de forma segura.

Crie um arquivo chamado .env na raiz do seu projeto e adicione as seguintes variáveis:

```bash
TELEGRAM_TOKEN=SEU_TOKEN_AQUI
TELEGRAM_CHAT_ID=SEU_CHAT_ID_AQUI
```

Substitua SEU_TOKEN_AQUI pelo token do seu bot (obtido no passo 1) e SEU_CHAT_ID_AQUI pelo ID do seu canal.

## 4. Executando o Script

Agora, você pode executar o script que irá realizar a busca dos produtos e enviar as informações para o Telegram.

Execute o seguinte comando:

```bash
python main.py
```

Ou, se preferir, você pode rodar o script de forma automatizada utilizando GitHub Actions, que pode ser configurado para rodar diariamente e enviar atualizações do preço para o Telegram.

## 5. Configuração do GitHub Actions

O projeto está configurado para rodar automaticamente todos os dias às 01:00 (horário de Brasília). Para isso, foi criado um workflow utilizando GitHub Actions. O arquivo de configuração está localizado em .github/workflows/web-scraping.yml.

Se você deseja rodar o workflow manualmente ou de forma agendada, o cronograma está configurado para rodar todos os dias às 01:00:

```bash
on:
schedule:
- cron: '0 4 * 11 *' # Executa todos os dias às 04:00 UTC (01:00 Brasília) somente em novembro
workflow_dispatch:  # Permite a execução manual também
```

## 6. Resultado

<div align="center">
  <img src="assets/telegram-webscrapingbot.png" width="30%" />
</div>

## 7. Contribuindo
Se você deseja apoiar este projeto, deixe um ⭐.

___

Feito com 💙 por [Marco Antonio](https://www.linkedin.com/in/mrk-silva/).