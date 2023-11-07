'''Crie um programa que leia o nome de uma pessoa
e diga se ela tem "SILVA" no nome.'''

nome = str(input("Digite seu nome completo: "))

nome = nome.upper()

if "SILVA" in nome:
    print("Seu nome tem SILVA!")
else:
    print("Seu nome NÃO tem SILVA!")
