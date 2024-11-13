# Web Scraping de Produtos e Envio via Telegram

Este projeto realiza a automação para buscar informações de preços de produtos no e-commerce **KaBuM!**, utilizando o **Playwright** para scraping e enviando as informações através de um **bot do Telegram**.

![Telegram Logo](assets/telegram_logo.png)  
*Logo do Telegram*

![Playwright Logo](assets/playwright_logo.png)  
*Logo do Playwright*

![KaBuM Logo](assets/kabum_logo.png)  
*Logo do KaBuM!*

## Funcionalidade

O script realiza as seguintes tarefas:

1. Pesquisa um produto no e-commerce **KaBuM!**.
2. Extrai informações como o preço antigo, preço novo, preço em parcelas e o link do produto.
3. Envia as informações obtidas para um **canal do Telegram** via bot.

## Tecnologias Utilizadas

- **Playwright**: Framework utilizado para realizar o scraping no site.
- **Telegram Bot API**: Para enviar as informações diretamente para um canal no Telegram.

## Pré-Requisitos

Antes de rodar o projeto, você precisará configurar o ambiente de desenvolvimento e criar um bot no Telegram. Siga as etapas abaixo para a configuração.

### 1. Criar um Bot no Telegram

Para criar um bot no Telegram, siga os seguintes passos:

1. Abra o Telegram e procure por **@BotFather**.
2. Envie o comando `/newbot` para criar um novo bot.
3. O BotFather pedirá para você nomear seu bot e criar um nome de usuário único (que termina com "bot").
4. Após a criação, você receberá um **token** do bot. Guarde este token, pois você precisará dele para a configuração do seu bot.

### 2. Criar um Canal no Telegram

Se você ainda não tem um canal, siga estas etapas:

1. No Telegram, crie um canal.
2. Adicione o bot recém-criado como administrador do canal.
3. Obtenha o **ID do canal**. Para isso, você pode usar o bot **@userinfobot** para descobrir o ID do seu canal. O ID será algo como `@channelusername` ou um número negativo (exemplo: `-123456789`).

### 3. Instalar Dependências

Para rodar o projeto, é necessário instalar algumas dependências. Siga as etapas abaixo:

#### 3.1 Clonar o Repositório

```bash
git clone https://github.com/mrk-qa/webscraping-playwright-product-kabum-e-commerce-bot-telegram.git
cd webscraping-playwright-product-kabum-e-commerce-bot-telegram
