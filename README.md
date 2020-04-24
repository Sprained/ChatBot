# ChatBot
 ChatBot feito em python, onde vc pode ensinalos respostas para cada pergunta.
 
## Uso
- Instalar dependencias encontrados no requirements.txt `$ pip install -r requirements.txt`

- Alterar `bot.inicia('Nome do contato')` na main.py

- Iniciar com `$ python main.py`

## Funcionamento
Ao iniciar o bot ele ira startar as funções o qual ele pode executar, que no momento se resume em aprender.

Ele pedira pra criar uma pasta chamaddo treino onde vc pode colocar um arquivo txt com infos para ele usar nas perguntas, exemplo como responder o Bom dia.

Para falar com o bot so usar o ::

E unico comando atual que ele sabe é o :: aprender, onde ele ira aprender uma resposta para uma pergunta.

Toda conversa que ele tiver, e oque ele aprender, sera salvo num sqlite que ele cria ao iniciar o bot a primeira vez.


## Melhorias
As melhorias o qual podem ser feitas, como ele é um chatbot, é fazer ele coletar legendas na web como uma database ou deixar ele escutando um grupo. Assim ele teria mais respostas antes de serem ensinadas para ele.

Essa base de dados pode ser manual caso queira, so colocar as legendas num arquivo txt na pasta treino.

## Implementação de Funções
Pode ser implementadas novas funções ao bot. No bot.py coloca essa a nova função o qual deseja que ele execute.

Caso seja uma função que precise de um comando, no main.py so colocar um elif com o comando e puxar a função.
