# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira
# e mostre quantos dolares ela pode comprar

real = float(input('Digite quantos reais voce tem na carteira: '))
dolar = real/3.27

print('Voce pode comprar {:.2f} dolares!'.format(dolar))
