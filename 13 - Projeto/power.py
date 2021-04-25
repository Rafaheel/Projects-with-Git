import pyautogui
from time import sleep


pyautogui.keyDown('winleft')
pyautogui.press(['d'])
pyautogui.keyUp('winleft')

sleep(3)

pyautogui.click('power.PNG', clicks=2)

sleep(60)

pyautogui.click('atualizar.PNG')

sleep(15)

pyautogui.click('fechar.PNG')

sleep(10)

pyautogui.click('salvar.PNG')