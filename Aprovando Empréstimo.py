'''Escreva um programa para aprovar o empréstimo bancário para a
compra de uma casa. Pergunte o valor da casa, o salário do
comprador e em quantos anos ele vai pagar. A prestação mensal
não pode exceder 30% do salário ou então o empréstimo será negado.'''

print("-=-"*20)
print("Verificação de Crédito...")
print("-=-"*20)

valor = float(input("Valor do imóvel desejado: "))
salario = float(input("Valor do salário recebido: "))
tempo = int(input("Período de pagamento (em anos): "))
mensalidade = valor /(tempo*12)

if mensalidade<=(0.3*salario):
    print("Para pagar o imovel de R${:.2f} em {} anos o valor da prestação será R$ {:.2f}".format(valor,tempo,mensalidade))
    print("Empréstimo CONCEDIDO!")
else:
    print("Para pagar o imovel de R${:.2f} em {} anos o valor da prestação será R$ {:.2f}".format(valor,tempo,mensalidade))
    print("Empréstimo NEGADO!")


    input("\n\nPress <enter> to continue...")
