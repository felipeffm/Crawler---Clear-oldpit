

# //TODO aquisição de dados historicos
# //TODO analise de dados historicos
        # //TODO aquisição de dados em tempo real
# //TODO comparação de dados em tempo real com resultados de analise historica
# //TODO decisao de compra ou venda
# //TODO acesso site e login de acesso



# //TODO integracao compra ou venda webservices
from selenium.webdriver.common.keys import Keys
from selenium import webdriver


def abrir_navegador():
    global driver

    driver = webdriver.Firefox()
    driver.get(r'https://novopit.clear.com.br/Operacoes/RendaVariavel/Basico')
    #usuario loga manualmente na clear
abrir_navegador()
    
""" esse html não ta com o xpath funcionando pq tem muitos eventos e o css ta 
carregado demais. Então a seleção vai ser por partes, primeiro as hierarquias maiores"""

lista_iframes = driver.find_elements_by_tag_name('iframe')
iframe = lista_iframes[2]
driver.switch_to.frame(iframe)
body = driver.find_element_by_tag_name('body')
lista_acoes = body.find_elements_by_class_name('asset-name')

#encontrar caixas de texto para 
import bs4
##quantidade
//*[@id="input-quantity"]
##preco limite
//*[@id="input-price"]
##assinatura eletrônica caso não esteja clicado "salvar"
<input type="password" placeholder="Assinatura Eletr." class="input-digital-sign-field" maxlength="7">
##botão de concluir acao

#checar se elementos estão ok

#estando ok, interagir com elementos

import selenium
from selenium import webdriver

browser = webdriver.Firefox()