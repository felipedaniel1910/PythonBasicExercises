''' Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
 Faça um programa que ajude ele, lendo o nome dos alunos e
 escrevendo na tela o nome do escolhido.'''

'''O mesmo professor do desafio 019 quer sortear a ordem de apresentação de
trabalhos dos alunos. Faça um programa que leia o nome dos quatro
alunos e mostre a ordem sorteada.'''

import random

aluno1 = str(input("Primeiro aluno: "))
aluno2 = str(input("Segundo aluno: "))
aluno3 = str(input("Treceiro aluno: "))
aluno4 = str(input("Quarto aluno: "))

lista = [aluno1,aluno2,aluno3,aluno4]

random.shuffle(lista)

print("A ordem da apresentação será: ")
print(lista)

input("\n\nPress <enter> to continue")
