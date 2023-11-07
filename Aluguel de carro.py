# Escreva um programa que pergunta a qunatidade de km percorridos
# por um carro alugado e a qunatidade de dias pelos quais ele
# foi alugado. Calcule o preço a pagar, sabendo que o carro custa
# R$60 por dia e R$0,15 por km rodado

km = float(input('Quantos km foram rodados: '))
dias = int(input('Por quantos dias o carro foi alugado:  '))

preco = km*0.15 + dias*60

print('O preço a ser pago é R${:.2f}!'.format(preco))
                 
