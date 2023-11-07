# Escreva um programa que leia um valor em metros e o exiba convertido
# em centímetros e milímetros

val_metro = float (input('Digite o valor em metros: '))
cent = val_metro*100
mil = val_metro*1000

print('O valor em centímetros é {} e em milímetros é {}'.format(cent, mil))
