import time
import os
import sys
try:
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.chrome.options import Options as ChromeOptions
    from selenium.webdriver.firefox.options import Options as FirefoxOptions
    from selenium.webdriver.edge.options import Options as EdgeOptions
    from selenium.webdriver.chrome.service import Service as ChromeService
    from selenium.webdriver.firefox.service import Service as FirefoxService
    from selenium.webdriver.edge.service import Service as EdgeService
    from selenium.common.exceptions import WebDriverException
except ImportError:
    print('Instalando dependências...')
    os.system(f'{sys.executable} -m pip install selenium')
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.chrome.options import Options as ChromeOptions
    from selenium.webdriver.firefox.options import Options as FirefoxOptions
    from selenium.webdriver.edge.options import Options as EdgeOptions
    from selenium.webdriver.chrome.service import Service as ChromeService
    from selenium.webdriver.firefox.service import Service as FirefoxService
    from selenium.webdriver.edge.service import Service as EdgeService
    from selenium.common.exceptions import WebDriverException

print('''\n==== DMS - Token Grabber ====
Este script irá abrir o Discord Web no navegador de sua escolha.
Faça login normalmente e, após o carregamento, pressione ENTER aqui para capturar o token.
''')

print('Escolha o navegador:')
print('[1] Chrome')
print('[2] Firefox')
print('[3] Edge')
navegador = input('Digite o número do navegador desejado: ').strip()

if navegador == '1':
    browser = 'chrome'
    driver_path = 'chromedriver'
    options = ChromeOptions()
    options.add_experimental_option('detach', True)
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument('--start-maximized')
    service = ChromeService(driver_path)
elif navegador == '2':
    browser = 'firefox'
    driver_path = 'geckodriver'
    options = FirefoxOptions()
    options.set_preference('dom.webdriver.enabled', False)
    options.set_preference('useAutomationExtension', False)
    options.add_argument('--start-maximized')
    service = FirefoxService(driver_path)
elif navegador == '3':
    browser = 'edge'
    driver_path = 'msedgedriver'
    options = EdgeOptions()
    options.add_argument('--start-maximized')
    service = EdgeService(driver_path)
else:
    print('Navegador inválido. Saindo...')
    sys.exit(1)

driver = None
try:
    if browser == 'chrome':
        driver = webdriver.Chrome(service=service, options=options)
    elif browser == 'firefox':
        driver = webdriver.Firefox(service=service, options=options)
    elif browser == 'edge':
        driver = webdriver.Edge(service=service, options=options)
except WebDriverException:
    print(f'Driver do navegador não encontrado. Baixe o driver correspondente à sua versão do navegador:')
    if browser == 'chrome':
        print('https://chromedriver.chromium.org/downloads')
    elif browser == 'firefox':
        print('https://github.com/mozilla/geckodriver/releases')
    elif browser == 'edge':
        print('https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/')
    input('Após baixar, coloque o executável na mesma pasta deste script e pressione ENTER...')
    if browser == 'chrome':
        driver = webdriver.Chrome(service=service, options=options)
    elif browser == 'firefox':
        driver = webdriver.Firefox(service=service, options=options)
    elif browser == 'edge':
        driver = webdriver.Edge(service=service, options=options)

# Abre o Discord Web
print('Abrindo Discord Web...')
driver.get('https://discord.com/login')

input('\nApós fazer login e ver seu Discord carregado, pressione ENTER aqui para capturar o token...')

# Executa JS para pegar o token do localStorage
try:
    token = driver.execute_script("return window.localStorage.getItem('token');")
    if token:
        print(f'\nSeu token é:\n{token}\n')
        with open('meu_token.txt', 'w') as f:
            f.write(token)
        print('Token salvo em "meu_token.txt".')
    else:
        print('Não foi possível capturar o token. Certifique-se de estar logado no Discord Web.')
except Exception as e:
    print(f'Erro ao capturar o token: {e}')

input('Pressione ENTER para sair...')
driver.quit() 