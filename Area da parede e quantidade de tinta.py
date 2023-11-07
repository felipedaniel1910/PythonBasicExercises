# Faça um programa que leia a largura e a
# altura de uma parede em metros, calcule a sua área e a quantidade
# de tinta necessaria para pinta-la, sabendo que cada litro de tinta
# pinta uma área de 2m^2

largura = float(input('Digite a largura da parede em metros: '))
altura = float(input('Digite a altura da parede em metros: '))

area = largura*altura
quant_tinta = area/2

print('São necessarias {:.2f} latas de tinta para pinta a parede de {:.2f} m²'.format(quant_tinta, area))
                     
