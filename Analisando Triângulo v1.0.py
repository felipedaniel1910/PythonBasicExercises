'''Desenvolva um programa que leia o comprimento de três retas e diga
ao usuário se elas podem ou não formar um triângulo.'''

'''REGRA MATEMATICA: Cada segmento deve ser menor do que a soma dos
outros dois...'''

print('-=-'*20)
print("Analisador de triângulos...")
print('-=-'*20)
r1 = float(input("Primeiro segmento: "))
r2 = float(input("Segundo segmento: "))
r3 = float(input("Tereiro segmento: "))

if r1<r2+r3 and r2<r1+r3 and r3<r1+r2:
    print("Esses seguimentos PODEM FORMAR um triângulo.")
else:
    print("Esses seguimentos NÃO PODEM formar um triângulo.")

