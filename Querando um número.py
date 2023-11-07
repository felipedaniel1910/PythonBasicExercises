# Crie um programa que leia um número Real qualquer
# pelo teclado e mostre na tela a sua porção Inteira.

from math import trunc

num = float(input("Digite um número real qualquer: "))

print("o numero digitado foi {} e a porção inteira do número é {}".format(num,trunc(num)))

print("o numero digitado foi {} e a porção inteira do número é {}".format(num,int(num)))
