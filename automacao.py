
# Passo 1 - Entrar no site

import pyautogui
import time

pyautogui.PAUSE = 0.8

pyautogui.hotkey("win", "s")
pyautogui.write("chrome")
pyautogui.press("enter")

time.sleep(2)

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

time.sleep(3)

# Passo 2 - Fazer login

pyautogui.click(x=699, y=494)
pyautogui.write("brubruno@gmail.com")
pyautogui.press("tab")
pyautogui.write("Senha123")
pyautogui.press("tab")
pyautogui.press("enter")

time.sleep(3)

# Passo 3 - Importar a base de produtos

import pandas

tabela = pandas.read_csv("produtos.csv")
print(tabela)

# Passo 4 - Cadastrar 1 produto
# Passo 5 - Repetir o cadastro para todos os produtos
for linha in tabela.index:

    pyautogui.click(x=846, y=345)
    pyautogui.write(str(tabela.loc[linha, "codigo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(str(obs))

    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(5000)

# Passo 5 - Repetir o cadastro para todos os produtos

