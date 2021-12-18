import pyautogui as pa
from time import sleep


# Criar uma função que da likes automaticamente 

def click(x, y):
    pa.moveTo(x, y)
    pa.click()

while True:
       # Verifica se o icone do like esta na tela 
    like = pa.locateOnScreen('Like(normal).png')

    if like != None:
        # Da um click no icone de like caso ele ainda não tenha sido "preenchido" 
        click(like.left, like.top)
        sleep(5)
        # Caso se ja houve um click no icone     
        
    else:
        sleep(1)
        print('| ━═━═━═━═━═━═━═━═━ |')
        
