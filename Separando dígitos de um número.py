'''Faça um programa que leia um número de 0 a 9999 e
mostre na tela cada um dos dígitos separados.'''

num = -1
while (num < 0 or num > 9999):
     num = int(input("Digite um numero de 0 à 9999: "))

x = str(num)

tam = len(x)

print("Os dígitos são: ")
for i in range (tam):
    print(x[i])


