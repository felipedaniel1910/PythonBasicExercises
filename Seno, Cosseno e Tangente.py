# Faça um programa que leia um ângulo qualquer e
# mostre na tela o valor do seno, cosseno e tangente desse ângulo

import math

ang_graus = float(input("Digite um ângulo em graus: "))
ang_rad = math.radians(ang_graus)

print("O Seno de {:.2f}  é {:.2f}, o Cosseno é {:.2f} e a Tangente é {:.2f}.".format(ang_graus,math.sin(ang_rad),math.cos(ang_rad), math.tan(ang_rad)))
