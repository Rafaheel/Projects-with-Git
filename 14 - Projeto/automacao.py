from os import pipe
import pyautogui
from time import sleep


# Limpa a Tela
pyautogui.keyDown('winleft')
pyautogui.press('d')
pyautogui.keyUp('winleft')

#pega a posição do icone do Chrome
posicao_navedador = pyautogui.position()
print(posicao_navedador)
sleep(1)
pyautogui.click(x=35, y=329, clicks=2)


#Pega a posiçao para digitar o endereço
posicao_navedador_end = pyautogui.position()
print(posicao_navedador_end)
sleep(1)
pyautogui.click(x=1610, y=60, clicks=1)
sleep(1)
pyautogui.write('https://www.globo.com/')
sleep(1)
pyautogui.press('enter')

#Pega a posiçao para digitar a pesquisa
posicao_campo_busca = pyautogui.position()
print(posicao_campo_busca)
pyautogui.moveTo(x=3034, y=128)
sleep(2)
pyautogui.click(x=3034, y=128, clicks=1)
sleep(1)
pyautogui.write('Futebol')
sleep(1)
pyautogui.press('enter')