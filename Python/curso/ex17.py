from math import hypot

cateto_adjacente = float(input('Informe a medida do cateto adjacente: '))
cateto_oposto = float(input('Informe a medida do cateto oposto: '))
hipotenusa = float(hypot(cateto_oposto, cateto_adjacente))
print(f'A hipotenusa deste triangulo mede {hipotenusa :.2f}')