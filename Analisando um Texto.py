'''Crie um programa que leia o nome completo de uma pessoa e mostre:
– O nome com todas as letras maiúsculas e minúsculas;
– Quantas letras ao todo (sem considerar espaços);
– Quantas letras tem o primeiro nome.'''

nome = str(input("Digite seu nome completo: "))

print(nome.upper())
print(nome.lower())

x = 0
for i in range (len(nome)):
    if nome[i] != " ":
        x = x + 1;

print("O numero de letras sem espaço é: {}!".format(x))

print("O primeiro nome tem {} letras.".format(len(nome.split()[1])))
