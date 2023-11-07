num1 = int (input("Digite o primeiro numero: "))
num2 = int (input("Digite o segundo numero: "))

aux = 0
a = num1
b = num2

if a < b:
    aux = a
    a = b
    b = aux

r = a % b

while r != 0:
    a = b
    b = r
    r = a % b


print("O MDC é: %i" %b)
mmc = (num1*num2)/b
print("O MMC é: %i" %mmc)



