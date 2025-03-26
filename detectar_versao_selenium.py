import selenium
from selenium import webdriver

# Detectar a versão do Selenium
selenium_version = selenium.__version__

if selenium_version.startswith('4'):
    from selenium.webdriver.chrome.service import Service
    # Configuração para Selenium 4.x
    def iniciar_driver(chromedriver_dir, options):
        service = Service(chromedriver_dir)
        driver = webdriver.Chrome(service=service, options=options)
        return driver
elif selenium_version.startswith('3'):
    # Configuração para Selenium 3.x
    def iniciar_driver(chromedriver_dir, options):
        driver = webdriver.Chrome(executable_path=chromedriver_dir, options=options)
        return driver