'''Crie um programa que leia o nome de uma cidade diga se
ela começa ou não com o nome "SANTO".'''

cidade = str(input("Digite o nume da cidade: "))

cidade = cidade.upper()

indice = cidade.find("SANTO")

if indice == 0:
    print("O nome da cidade COMEÇA com SANTO!")
else:
    print("O nome da cidade NÃO começa com SANTO!")
