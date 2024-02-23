#:four_leaf_clover: MegaSena Telegram bot :four_leaf_clover:

- Esse script tem como objetivo facilitar a conferência de apostas feitas na MegaSena

- Utilizando a api: https://servicebus2.caixa.gov.br/portaldeloterias/api/megasena/

###:pushpin: Utilizando o script:

```bash
# Faça o clone deste repositório:

git clone https://github.com/FelippeBritto/megasena-telegram-bot.git
```

###:pushpin: .env

- Crie um arquivo .env no mesmo diretório contendo:

```ts
// Token obtido ao criar seu bot no telegram
TELEGRAM_BOT_TOKEN = "TOKEN_DO_SEU_BOT";

// ID do chat em que deseja enviar as mensagens
TELEGRAM_GROUP_ID = "ID_DO_GRUPO";

//(Opcional) Suas apostas podem ser adicionadas no .env EX.:
JOGO_1 = ["0", "0", "0", "0", "0", "0"];

// Ao adicionar as apostas ajuste a variável nossos_jogos para a sua quantidade de jogos

// Caso não queira adicionar as apostas no .env, apenas altere os valores em nossos_jogos
```

###:pushpin: Telegram bot

- Para criar o seu bot no telgram, abra o app e pesquise nos chats por BotFather

- Inicie a conversa com /start

- Siga os passos no chat e ao final obterá o token para utilizar neste script

###:pushpin: Group ID

- Adicione o bot em um grupo

- Abra o telegram no pc

- Acesse o grupo em que adicionou o bot

- Inpecione o nome do grupo

- Procure o data-peer-id
