
n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))

s = n1+n2
m = n1*n2
d = n1/n2
di = n1//n2 # Divisao inteira
e = n1** n2 # potencia (pode ser ("pow(n1,n2)"))

print('A soma é {}, o produto é {} e a divisão é {:.3}'.format(s,m,d)) #usamos {:.3} para limitar o numero float à 3 digitos- ou {:.3f}
print('A divisão inteira é {} e a potência é {}'.format(di,e))

# OBS: para nao quebrar linha colocamos- print("Digite algo", end = '')
# OBS: para quebrar a linha no meio da sentença = print("Digite \n Algo")
