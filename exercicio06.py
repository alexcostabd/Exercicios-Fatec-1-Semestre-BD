## Um dado comerciante maluco cobra 10% de acréscimo para cada prestação em atraso
## e depois dá um desconto de 10% sobre esse valor. Faça um algoritmo que solicite o
## valor da prestação em atraso e apresente o valor final a pagar, assim como o prejuízo do
## comerciante na operação.

valor_prestacao = float(input("Valor da prestação: "))
valor_com_acrescimo = valor_prestacao * 1.1
valor_com_desconto = valor_com_acrescimo - (valor_com_acrescimo * 1.1 - valor_com_acrescimo)
print("Valor acrescido: R$ {:.2f}\nValor com desconto: R$ {:.2f}\nValor final: R$ {:.2f}\nPrejuízo: R$ {:.2f}".format(valor_com_acrescimo, valor_com_desconto, valor_com_desconto, valor_com_acrescimo - valor_com_desconto))