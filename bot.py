import os 
import time
import re
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
from selenium import webdriver

class wppbot:

    dir_path = os.getcwd()

    def __init__(self, role):
        self.bot = ChatBot(role)
        self.bot.set_trainer(ListTrainer)

        self.chrome = self.dir_path+'\chromedriver.exe'

        self.options = webdriver.ChromeOptions()
        self.options.add_argument(r'user-data-dir='+self.dir_path+'\profile\wpp')
        self.driver = webdriver.Chrome(self.chrome, chrome_options=self.options)

    def inicia(self, Gasosa):

        self.driver.get('https://web.whatsapp.com/')
        self.driver.implicitly_wait(15)

        self.caixa_de_pesquisa = self.driver.find_element_by_class_name('_2MSJr')

        self.caixa_de_pesquisa.send_keys(Gasosa)
        time.sleep(2)
        print(Gasosa)
        self.contato = self.driver.find_element_by_xpath('//span[@title = "{}"]'.format(Gasosa))
        self.contato.click()
        time.sleep(2)

    