'''Faça um programa que leia uma frase pelo teclado e mostre quantas vezes
aparece a letra "A", em que posição ela aparece a primeira vez e em que
posição ela aparece a última vez.'''

frase = str(input("Digite uma frase: ")).upper().strip() #strip elimina espaços 

print("A letra 'A' aparece {} vezes!".format(frase.count("A")))
print("A letra 'A' aparece pela primeira vez na posição {}!".format(frase.find("A")+1))
print("A letra 'A' aparece pela ultima vez na posição {}!".format(frase.rfind("A")+1))

for i in range (len(frase)):
    if frase[i] == "A":
        posicao = i

print("A letra 'A' aparece pela ultima vez na posição {}!".format(posicao+1))
