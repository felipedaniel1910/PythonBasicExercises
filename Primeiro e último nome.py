'''Faça um programa que leia o nome completo de uma pessoa,
mostrando em seguida o primeiro e o último nome separadamente.'''

nome = str(input("Digite seu nome completo: ")).strip().title()

print("Seu primeiro nome é {} e seu ultimo nome é {}.".format(nome.split()[0],nome.split()[len(nome.split())-1]))


input("\n\nPress <enter> to continue...")
