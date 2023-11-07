# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente
# de um triângulo retângulo.Calcule e mostre o comprimento da hipotenusa.

from math import sqrt
from math import pow
from math import hypot

cat1 = float(input("Digite o comprimento do primeiro cateto: "))
cat2 = float(input("Digite o comprimento do segundo cateto: "))

hip1 = ((cat1**2)+(cat2**2))**0.5

hip2 = sqrt((pow(cat1,2))+(pow(cat2,2)))

hip3 = hypot(cat1,cat2)

print("O valor da hipotenusa pelo método 1 é {}".format(hip1))
print("O valor da hipotenusa pelo étodo 2 é {}".format(hip2))
print("O valor da hipotenusa pelo método 3 é {}".format(hip3))
