'''Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo
que ele foi multado. A multa vai custar R$7,00 por cada
Km acima do limite.'''

speed = int(input("Digite a sua velocidade: "))

if speed > 80:
    print("Você foi multado no valor de R$ {},00.".format((speed-80)*7))
else:
    print("Tenha uma ótima viagem!")

input("Press <enter> to continue...")

