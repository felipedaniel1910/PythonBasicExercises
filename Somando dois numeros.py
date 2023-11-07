# Crie um script que leia dois numeros e tente mostrar a soma entre eles

num1 = int(input ('Digite o primeiro numero: '))
num2 = int(input ('Digite o segundo numero: '))

print('A soma entre eles é:', num1+num2)
#ou
print('A soma entre eles é: {}'.format(num1+num2))
#ou
print('A soma entre {} e {} vale {}'.format(num1, num2, num1+num2))

# OBS: É necessario um 'input' com 'int' porque senão ele entende como uma string



