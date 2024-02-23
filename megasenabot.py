# -*- coding: utf-8 -*-
from telegram import Bot
from requests.exceptions import SSLError
from dotenv import load_dotenv
import requests
import asyncio
import os

load_dotenv()

TOKEN = os.environ['TELEGRAM_BOT_TOKEN']

GROUP_ID = os.environ['TELEGRAM_GROUP_ID']

nossos_jogos = {
    "1. ": os.environ['JOGO_1'],
    "2. ": os.environ['JOGO_2'],
    "3. ": os.environ['JOGO_3'],
    "4. ": os.environ['JOGO_4'],
    "5. ": os.environ['JOGO_5'],
    "6. ": os.environ['JOGO_6'],
}

def obter_dados_loterias():
    try:
        response = requests.get('https://servicebus2.caixa.gov.br/portaldeloterias/api/megasena/', verify=False)
        if response.status_code == 200:
            return response.json()
    except SSLError as e:
        print("Erro de SSL:", e)
        return None

async def obter_mensagem_da_api():
    global loteria_resultados, loteria_proximo_concurso 
    loteria = obter_dados_loterias()
    loteria_resultados = loteria['listaDezenas']
    loteria_proximo_concurso = loteria['dataProximoConcurso']

    mensagem = (
        f"🍀 <b>Resultado da {loteria['tipoJogo']}</b> 🍀\n"
        f"<b>Dia: {loteria['dataApuracao']}</b>\n"
        f"<b>Concurso:</b> {loteria['numero']}\n"
        f"<b>Resultado:</b> {', '.join(loteria['listaDezenas'])} \n"
        f"<b>Próximo concurso:</b> {loteria['dataProximoConcurso']}"
    )

    return mensagem

async def verificar_acertos():
    acertos = []
    for jogo_nome, jogo_numeros in nossos_jogos.items():
        num_acertos = sum(1 for numero in loteria_resultados if numero in jogo_numeros)
        if num_acertos == 4:
            acertos.append(f"<b>{jogo_nome}</b> {jogo_numeros}\n Obteve quadra. 🤑\n")
        elif num_acertos == 5:
            acertos.append(f"<b>{jogo_nome}</b> {jogo_numeros}\n Obteve quina. 🤑\n")
        elif num_acertos == 6:
            acertos.append(f"<b>{jogo_nome}</b> {jogo_numeros}\n Obteve sena. 🤑\n")
        else:
            acertos.append(f"<b>{jogo_nome}</b> {jogo_numeros}\n Não obteve prêmio. 😿\n")
    return acertos

async def enviar_mensagem():
    bot = Bot(token=TOKEN)
    dados_sorteio = await obter_mensagem_da_api()
    resultado_apostas = await verificar_acertos()

    await bot.send_message(chat_id=GROUP_ID, text=dados_sorteio, parse_mode='HTML')
    await bot.send_message(chat_id=GROUP_ID, text="\n".join(resultado_apostas), parse_mode='HTML')

async def run_bot():
    await enviar_mensagem()

asyncio.run(run_bot())