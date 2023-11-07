'''Escreva um programa que faça o computador "pensar" em um número inteiro
entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número
escolhido pelo computador. O programa deverá escrever na tela se o
usuário venceu ou perdeu.'''

from random import randint

computador = randint(0,5) # faz o cumputador sortear um numero

print("-=-"*20)

print("Vou pensar em um número de 0 à 5. Tente adivinhar...")

print("-=-"*20)

jogador = int(input("Em que número eu pensei? "))

if jogador == computador:
    print("Parabéns, você aceertou!!!")
else:
    print("Que pena, você errou :( ")
    

