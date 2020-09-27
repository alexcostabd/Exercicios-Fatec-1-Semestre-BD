def cabecalhoPagamento():
    print("=_="*38)
    print("=_="*2 + "  "*19 + "ÁREA DE PAGAMENTO "+ "  "*23 +"=_="*2)
    print("=_="*38)
    print("|"+"   "*2 + "1 - A vista em dinheiro ou cheque, recebe 10 porcento de desconto "+"  "*20+"|" )
    print("|"+"   "*2 + "2 - A vista no cartão de crédito, recebe 5 porcento de desconto "+"  "*21+"|" )
    print("|"+"   "*2 + "3 - Em duas vezes, preço normal de etiqueta sem juros "+"  "*26+"|" )
    print("|"+"   "*2 + "4 - Em três vezes, preço normal de etiqueta mais juros de 10 porcento "+"  "*18+"|" )
    print("=_="*38)
    print("=_="*2 + "  "*19 + "SELECIONE A OPÇÃO "+ "  "*23 +"=_="*2)    
    print("=_="*38)

def calculaPagamento(codigo, valor):
    if codigo == 1:
        valorPagamento = valor - (valor * 0.10)
        return valorPagamento
    elif codigo == 2:
        valorPagamento = valor - (valor * 0.05)
        return valorPagamento
    elif codigo == 3:
        valorPagamento = valor
        return valorPagamento
    else:
        valorPagamento = valor + (valor * 0.10)
        return valorPagamento

def main():
    cabecalhoPagamento()
    while True:

        selecao = int(input("DIGITE A OPÇÃO DE PAGAMENTO: "))
        while selecao <=0 or selecao >=5:
            print("Selecione uma opção válida! ")
            selecao = int(input("DIGITE A OPÇÃO DE PAGAMENTO:: "))

        valor = float(input("Digite o valor a ser pago: "))
        print("Valor a ser pago R${:.2f}".format(calculaPagamento(selecao, valor)))

        escolha = int(input(" 1 - Novo Pagamento\n 2 - finalizar\nDigite: "))
        if escolha == 2: break


if  __name__ == "__main__":
    main()

