import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import os

#                              # 
#                              #
#            FUNCOES           #
#                              #
#
#                              #   

def CaminhoAppdata():
        var_path = os.getenv('userprofile')
        caminho = var_path + r"\appdata\Local\Google\Chrome\User Data"
        return caminho

def ListaPerfilsChrome(caminho):
    lista_arquivos = os.listdir(caminho)
    lista_profile = [profile for profile in lista_arquivos if profile.startswith("Profile") ]
    dicionario_ext = {}
    for profile in lista_profile:
        # Caminho absoluto para um arquivo em outro diretório
        caminho_comprofile = (os.path.join(caminho, profile)) + r"\preferences"
        #abrindo o arquivo 
        with open(caminho_comprofile, 'r', encoding='utf-8') as arquivo:
            texto = arquivo.read()
        palavra_chave = "account_tracker_service_last_update"

        indice = texto.find(palavra_chave)
        
        # Verificar se a palavra foi encontrada
        if indice != -1:
            # Cortar tudo após a palavra, inclusive a própria palavra
            resultado = texto[:indice + len(palavra_chave)]
            inicio = texto.find('email"')
            fim = texto.find('","f')
            resultado = resultado[inicio:fim]
            resultado =resultado.replace('email":"',"")
            dicionario_int = {"perfil": profile}
            dicionario_ext[resultado] = dicionario_int
            
        else:
            resultado = "Indisponivel" +profile
    return dicionario_ext
    

def SeleniumChrome(PastaChrome,Perfil):
    # Caminho para o diretório do perfil de usuário


    # Configurando as opções do Chrome
    options = Options()
    options.add_argument(f"user-data-dir={PastaChrome}")
    options.add_argument(f"profile-directory={Perfil}")

    driver = webdriver.Chrome(options=options)

    driver.get("https://accounts.google.com/addsession")
    time.sleep(2)
    #li = /html/body/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div/form/span/section/div/div/div/div/ul/li[1]
    #li = /html/body/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div/form/span/section/div/div/div/div/ul/li[2]/div/div[1]/div/div[2]/div[2]
          #/html/body/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div/form/span/section/div/div/div/div/ul/li[4]/div/div[1]/div/div[2]/div[2]
          #/html/body/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div/form/span/section/div/div/div/div/ul/li[1]/div
    valor = driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div/form/span/section/div/div/div/div/ul/li[1]/div/div[1]/div/div[2]/div[2]").text
    print(valor)
    liVal = 1
    emails = []
    
    while True:
        try: 
            strval = str(liVal)
            email = driver.find_element(By.XPATH,f"/html/body/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div/form/span/section/div/div/div/div/ul/li["+strval+"]/div/div[1]/div/div[2]/div[2]").text
            emails.append(email)
            
            liVal +=1
        except:
            print("fim da lista")
            break
        print(emails)
    driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div/form/span/section/div/div/div/div/ul/li[1]").click()
    time.sleep(2)
    timeout = 100
    #criar variavel que pega do BD a senha
    senha = " o que vai pegar do banco"

    # Espera até que o elemento esteja presente no DOM e seja visível
    driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[2]/div/div/div/form/span/section[2]/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input").send_keys(senha)
    time.sleep(2)
    driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[3]/div/div[1]/div/div/button").click()
    time.sleep(10)



#print(valor["ti@fattorcredito.com.br"]["perfil"])
path = CaminhoAppdata()
perfil = ListaPerfilsChrome(path)['marcello.junior@fattorcredito.com.br']['perfil']
SeleniumChrome(path,perfil)
