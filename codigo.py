# PASSO A PASSO PROJETO 

# biblioteca para automatizar teclado, mouse e tela)
import pyautogui
import time
import pandas as pd

pyautogui.PAUSE = 0.5

# pyautogui.click -> clicar com o mouse
# pyautogui.write -> escrever com o teclado
# pyautogui.prMOLO000192ess -> pressionar uma tecla do teclado
# pyautogui.hotkey -> apertar um conjunto de teclas (ctrl c, Alt Tab)

# 1. abrir o navegador
pyautogui.press ("win")
pyautogui.write ("chrome")
pyautogui.press ("enter")

# 2. entrar no sistema
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter") 

# 2.1 tempo de carregamento para garantir a abertura do site completo
time.sleep(5) 

# 3. fazer login
pyautogui.click(x=526, y=351)
pyautogui.write("alle_andrade123@hotmail.com")
pyautogui.press("tab")
pyautogui.write("12345")
pyautogui.click(x=691, y=487)
# 4. abrir/importar base de dados para cadastrar
# 4.1 instalar bibliotecas para planilhas -> pip install pandas numpy openpyxl 

tabela = pd.read_csv("produtos.csv")

# 5. cadastrar um produto  
# str = string = texto
for linha in tabela.index: 
    codigo = str(tabela.loc[linha, "codigo"])
    # 5.1 clicar no campo produto
    pyautogui.click(x=473, y=255)
    # 5.2 digitar o produto   
    pyautogui.write(codigo)
    # passar para proximo campo
    pyautogui.press("tab")
    # marca
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    # passar para proximo campo
    pyautogui.press("tab")
    # tipo
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    # passar para proximo campo
    pyautogui.press("tab")
    # categoria
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    # passar para proximo campo
    pyautogui.press("tab")
    # preço
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    # passar para proximo campo
    pyautogui.press("tab")
    # custo
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    # passar para proximo campo
    pyautogui.press("tab")
    # obs
    obs = str(tabela.loc[linha, "obs"]) 
    if obs != "nan":
        pyautogui.write(obs)
    # passar para proximo campo
    pyautogui.press("tab")
    # apertar o botão enter
    pyautogui.press("enter")
    # subir para o topo da página
    pyautogui.scroll(5000) #ou pyautogui.press("home")

# 6. repetir até a lista acabar
