import re
from bot import wppbot

name = input('Digite o nome do contato ou grupo: ')

bot = wppbot('botin')
bot.treina('treino')
bot.inicia(name)
bot.saudacao(['Bot: Ola', 'Bot: Use :: no incio para falar comigo', 'Bot: Me ensine coisas pra mim ;). Use Aprender ou Ensinar pra isso.', 'Bot: Estarei observando as conversas e aprendendo :D'])
ultimo = ''

while True:
    texto = bot.escuta()
    # bot.escutaUsuario()
    # bot.observar(texto)
    if texto != ultimo and re.match(r'^::', texto):
        ultimo = texto
        texto = texto.replace('::', '')
        texto = texto.lower()
        if(texto == 'aprender' or texto == ' aprender' or texto == 'ensinar' or texto == ' ensinar'):
            bot.aprender(texto,'bot: Escreva a pergunta e após o ? a resposta.','bot: Obrigado!','bot: Você escreveu algo errado! Tente novamente...')
        # elif(texto == 'user' or  texto == ' user'):
        #     bot.escutaUsuario()
        else:
            bot.responde(texto)