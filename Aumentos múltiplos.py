'''Escreva um programa que pergunte o salário de um funcionário e
calcule o valor do seu aumento. Para salários superiores a
R$1250,00, calcule um aumento de 10%. Para os inferiores ou
iguais, o aumento é de 15%.'''

print("Precisamos saber seu salário para calcularmos o valor do seu aumento...")
salario = int(input("Digite o seu salário: "))

if salario>1250:
    print("Seu aumento srá de R$ {}!".format(salario*0.1))
else:
    print("Seu aumento srá de R$ {}!".format(salario*0.15))

input("\n\nPress <enter> to continue...")
