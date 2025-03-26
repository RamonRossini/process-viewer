from decouple import config
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

# Informações do .env
meu_cpf = config('MEU_CPF')
empresa_cnpj = config('EMPRESA_CNPJ')

def realizar_consulta():

    # Configuração inicial
    service = Service('./chromedriver.exe')
    driver = webdriver.Chrome(service=service)

    # Acessar o site
    driver.get('https://esaj.tjsp.jus.br/cpopg/open.do')

    # Localizar o select e selecionar a opção
    select_element = driver.find_element(By.ID, 'cbPesquisa')
    dropdown = Select(select_element)
    dropdown.select_by_value('DOCPARTE')

    # Localizar o campo de consulta e enviar o texto
    campo = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'campo_DOCPARTE'))
    )
    campo.send_keys(meu_cpf)
    # campo.send_keys(empresa_cnpj)

    # Localizar e clicar no botão
    botao = driver.find_element(By.ID, 'botaoConsultarProcessos')
    botao.click()

    # Esperar que os resultados carreguem (opcional: adicionar espera explícita)
    driver.implicitly_wait(10)  # Espera implícita de até 10 segundos

    # Capturar os resultados
    try:
        resultados = driver.find_element(By.ID, 'tablePartesPrincipais').text
    except:
        resultados = 'Nenhum resultado encontrado'

    # Fechar o navegador
    driver.quit()

    return resultados