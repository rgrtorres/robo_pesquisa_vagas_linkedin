from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import PySimpleGUI as sg

sg.theme('DarkAmber')

layout = [
    [sg.Text('Bem vindo ao buscador de vagas.')],
    [sg.InputText()],
    [sg.Button('Ok'), sg.Button('Cancel')]
]

window = sg.Window('Pesquisar:', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break

    window.close()

    navegador = webdriver.Chrome(r'.\chromedriver.exe')
    navegador.get('https://www.linkedin.com/login/')
    navegador.maximize_window()

    email = navegador.find_element_by_id('username')
    email.send_keys('--EMAIL--')

    senha = navegador.find_element_by_id('password')
    senha.send_keys('--SENHA--')

    btn_login = navegador.find_element_by_xpath("//button[@type='submit']")
    btn_login.click()

    time.sleep(3)

    busca = navegador.find_element_by_xpath("//input[@placeholder='Pesquisar']")
    busca.send_keys(values[0])
    busca.send_keys(Keys.RETURN)

    time.sleep(3)

    filtro_vagas = navegador.find_element_by_xpath("//button[@aria-label='Vagas']")
    filtro_vagas.click()

    time.sleep(2)

    filtro_remoto = navegador.find_element_by_xpath("//button[@aria-label='Filtro Remoto.']")
    filtro_remoto.click()

    input('')

window.close()