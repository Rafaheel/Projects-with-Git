import random

n1 = input("informe o primeiro nome: ")
n2 = input("informe o segundo nome: ")
n3 = input("informe o terceiro nome: ")
n4 = input("informe o quarto nome: ")
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)

print(f'Quem vai apagar o quadro hoje é {escolhido}')