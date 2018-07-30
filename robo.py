from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

contatos =[] #Nomes das pessoas que quero enviar a msg.
msg = input("Mensagem: ")

def start_robo():
    drive = webdriver.Chrome('/home/andre/drive/chromedriver')
    drive.get("https://web.whatsapp.com")
    input("Aguardando Ler QR Code") #Codigo manual
    sleep(3)
    for contato in contatos:
        cx_pesquisa = drive.find_element_by_class_name('_2MSJr')
        cx_pesquisa.send_keys(dados)
        cx_pesquisa.send_keys(Keys.ENTER)
        cx_msg = drive.find_element_by_class_name("_2S1VP")
        cx_msg.send_keys(msg)
        bt_enviar = drive.find_element_by_class_name('_35EW6')
        bt_enviar.click()


start_robo()
