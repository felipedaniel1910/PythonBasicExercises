# Faça um programa que leia um numero inteiro qualquer
# e mostre na tela a sua tabuada

num = int(input('Digite um numero inteiro: '))

for i in range (1,10):
    res = num*i
    print('{}X{}= {}'.format(num, i , res))
    
