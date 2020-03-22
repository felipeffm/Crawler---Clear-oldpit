

# //TODO aquisição de dados historicos
# //TODO analise de dados historicos
# //TODO aquisição de dados em tempo real
# //TODO comparação de dados em tempo real com resultados de analise historica
# //TODO decisao de compra ou venda
# //TODO acesso site e login de acesso



# //TODO integracao compra ou venda webservices
"""Script para instalação geckodriver no ubuntu--> install_gecko.sh"""
#from selenium.webdriver.common.keys import Keys
from selenium import webdriver
#from selenium.webdriver.firefox.options import Options
#from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
#binary = FirefoxBinary('/snap/bin/firefox')
from selenium.webdriver.firefox.options import Options
opts = Options()
opts.log.level = "trace"
#options = Options()
#options.add_argument("-profile")
# put the root directory your default profile path here, you can check it by opening Firefox and then pasting 'about:profiles' into the url field 
#options.add_argument("/firefox_profile")
browser=webdriver.Firefox(executable_path = 'geckodriver',options=opts)
#from selenium.webdriver.chrome.options import Options
#options = Options()
#options.binary_location = r'/bin/'
#driver = webdriver.Chrome('chromedriver', options = options)
#entrar no site
def abrir_navegador():
    global driver
    
    #web e é argumento do objeto que é o próprio navegador.
    #ptions = Options()
    #ptions.add_argument("--user-data-dir=/usr/lib/chromium-browser")
    #options.add_argument("--headless") 

#    driver = webdriver.Firefox()
    driver = webdriver.Firefox()
    time.sleep(3)
    #Acesso do site wpp web pelo navegador
    driver.get('https://web.whatsapp.com/')
    #tempo de espera para carregar a página do wpp web.
    time.sleep(10)
#clicar no botao de compra ou de venda

#encontrar caixas de texto para 
##quantidade
##preco limite
##assinatura eletrônica caso não esteja clicado "salvar"
##botão de concluir acao

#checar se elementos estão ok

#estando ok, interagir com elementos

import selenium
from selenium import webdriver

browser = webdriver.Firefox()