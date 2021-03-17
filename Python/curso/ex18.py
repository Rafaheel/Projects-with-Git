import math

angulo = float(input('Informe o angulo que deseja saber: '))

seno = math.sin(math.radians(angulo))
print(f'o Seno é {seno :.2f}')

coseno = math.cos(math.radians(angulo))
print(f'O coseno é {coseno :.2f}')

tangente = math.tan(math.radians(angulo))
print(f'A tangente é {tangente :.2f}')
