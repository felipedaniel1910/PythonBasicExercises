var = input('Digite algo: ')

print('Tipo da variavel:',type(var)) #Verifica o tipo de dado
print('Contem apenas espaços:',var.isspace()) #Verifica se tem somente espaços
print('É numerico:',var.isnumeric()) #verifica se é um valor numerico
print('Tudo maiusculo:',var.isupper()) #Verifica se é tudo maiusculo
print('Tudo minusculo:',var.islower()) #Verifica se é tudo minusculo
print('É alfabetico:',var.isalpha()) #Verifica se é alfabético (letras)
print('É alfanumerico:',var.isalnum()) #Verifica se é alfabético e numérico (misturado ou nao)
print('Esta capitalizado:',var.istitle()) #Verifica se esa capitalizada (primeira letra maiuscula)
