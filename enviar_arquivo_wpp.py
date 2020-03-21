# -*- coding: utf-8 -*-
#Esse modulo anexa uma foto ou arquivo ao webwpp acessado pelo Selenium.
#A pagina do wppweb precisa estar aberta pelo selenium, e a conversa para enviar selecionada. 
import win32com.client as comclt
import time
#primeiro é preciso escolher se vai enviar foto ou um arquivo. 
#click no botao de anexar e depois na opcao de anexar fotos e videos ou documentos
def abrir_OpenFile(midia_ou_documento, driver):
    time.sleep(3)
    botao_anexar = driver.find_element_by_xpath('//*[@id="main"]/header/div[3]/div/div[2]/div')
    botao_anexar.click()
    time.sleep(0.3)
    if midia_ou_documento == 'midia':
        selecao_fotos_e_videos = driver.find_element_by_xpath( '//*[@id="main"]/header/div[3]/div/div[2]/span/div/div/ul/li[1]/button')
        time.sleep(0.3)
        selecao_fotos_e_videos.click()
    elif midia_ou_documento == 'documento':
        selecao_documento = driver.find_element_by_xpath('//*[@id="main"]/header/div[3]/div/div[2]/span/div/div/ul/li[3]/button')
        time.sleep(0.3)
        selecao_documento.click()
    else:
        print("faltou selecionar se é midia ou documento")

def selecionar_arquivo(path, driver):
    file_path = path
    windowsShell = comclt.Dispatch("WScript.Shell")
    windowsShell.SendKeys(file_path)
    windowsShell.SendKeys("{ENTER}")
    time.sleep(1)
    botao_enviar = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/span[2]/div/div')
    time.sleep(0.3)
    botao_enviar.click()
    time.sleep(0.3)
