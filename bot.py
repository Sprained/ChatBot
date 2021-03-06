import os 
import time
import re
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
from selenium import webdriver

class wppbot:

    dir_path = os.getcwd()

    def __init__(self, nome_bot):
        print(self.dir_path)
        self.bot = ChatBot(nome_bot)
        self.bot.set_trainer(ListTrainer)

        self.chrome = self.dir_path+'\chromedriver.exe'

        self.options = webdriver.ChromeOptions()
        self.options.add_argument(r"user-data-dir="+self.dir_path+"\profile\wpp")
        self.driver = webdriver.Chrome(self.chrome, chrome_options=self.options)

    def inicia(self, nome_contato):

        self.driver.get('https://web.whatsapp.com/')
        self.driver.implicitly_wait(15)

        self.caixa_de_pesquisa = self.driver.find_element_by_class_name('C28xL')

        self.caixa_de_pesquisa.send_keys(nome_contato)
        time.sleep(2)
        print(nome_contato)
        self.contato = self.driver.find_element_by_xpath('//span[@title = "{}"]'.format(nome_contato))
        self.contato.click()
        time.sleep(2)

    def saudacao(self, frase_inicial):
        self.caixa_de_mensagem = self.driver.find_element_by_class_name('_1Plpp')

        if type(frase_inicial) == list:
            for frase in frase_inicial:
                self.caixa_de_mensagem.send_keys(frase)
                time.sleep(1)
                self.botao_enviar = self.driver.find_element_by_class_name('_35EW6')
                self.botao_enviar.click()
                time.sleep(1)
        else:
            return False

    def escuta(self):
        post = self.driver.find_elements_by_class_name('_3_7SH')
        ultimo = len(post) - 1
        texto = post[ultimo].find_element_by_css_selector('span.selectable-text').text
        return texto

    # def escutaUsuario(self):
    #     post = self.driver.find_elements_by_class_name('_3_7SH')
    #     ultimo = len(post) - 1
    #     texto = ultimo.find_element_by_css_selector('_3FXB1').text
    #     print(texto)
        # self.caixa_de_mensagem = self.driver.find_element_by_class_name('_1Plpp')
        # self.caixa_de_mensagem.send_keys(name)
        # time.sleep(1)
        # self.botao_enviar = self.driver.find_element_by_class_name('_35EW6')
        # self.botao_enviar.click()
        # time.sleep(1)
        # return name

    # def observar(self, ultimo):
    #     while True:
    #         texto = self.escuta()
    #         if texto != ultimo:
    #             ultimo = texto
    #             texto = texto.lower()
    #             self.bot.train(texto)
    #             return ultimo
    #         else:
    #             ultimo = texto

    def aprender(self, ultimo, incial, final, erro):
        self.caixa_de_mensagem = self.driver.find_element_by_class_name('_1Plpp')
        self.caixa_de_mensagem.send_keys(incial)
        time.sleep(1)
        self.botao_enviar = self.driver.find_element_by_class_name('_35EW6')
        self.botao_enviar.click()
        time.sleep(1)
        self.x = True
        while self.x == True:
            texto = self.escuta()
            if texto != ultimo and re.match(r'^::', texto):
                if texto.find('?') != -1:
                    ultimo = texto
                    texto = texto.replace('::', '')
                    texto = texto.lower()
                    texto = texto.replace('?', '?*')
                    texto = texto.split('*')
                    novo = []
                    for elemento in texto:
                        elemento = elemento.strip()
                        novo.append(elemento)

                    self.bot.train(novo)
                    self.caixa_de_mensagem.send_keys(final)
                    time.sleep(1)
                    self.botao_enviar = self.driver.find_element_by_class_name('_35EW6')
                    self.botao_enviar.click()
                    self.x = False
                    return ultimo
                else:
                    self.caixa_de_mensagem.send_keys(erro)
                    time.sleep(1)
                    self.botao_enviar = self.driver.find_element_by_class_name('_35EW6')
                    self.botao_enviar.click()
                    self.x = False
                    return ultimo
            else:
                ultimo = texto


    def responde(self, texto):
        response = self.bot.get_response(texto)
        response = str(response)
        response = 'bot: ' + response
        self.caixa_de_mensagem = self.driver.find_element_by_class_name('_1Plpp')
        self.caixa_de_mensagem.send_keys(response)
        time.sleep(1)
        self.botao_enviar = self.driver.find_element_by_class_name('_35EW6')
        self.botao_enviar.click()
        time.sleep(1)

    def treina(self, nome_pasta):
        for treino in os.listdir(nome_pasta):
            conversas = open(nome_pasta+'/'+treino, 'r').readlines()
            self.bot.train(conversas)