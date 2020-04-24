import re
from bot import wppbot

bot = wppbot('botin')
bot.treina('treino')
bot.inicia('Miguel Resende')
bot.saudacao(['Bot: Ola', 'Bot: Use :: no incio para falar comigo', 'Me ensine coisas pra mim ;). Use Aprender ou Ensinar pra isso.'])
ultimo = ''

while True:
    texto = bot.escuta()
    if texto != ultimo and re.match(r'^::', texto):
        ultimo = texto
        texto = texto.replace('::', '')
        texto = texto.lower()
        if(texto == 'aprender' or texto == ' aprender' or texto == 'ensinar' or texto == ' ensinar'):
            bot.aprender(texto,'bot: Escreva a pergunta e após o ? a resposta.','bot: Obrigado!','bot: Você escreveu algo errado! Tente novamente...')
        else:
            bot.responde(texto)