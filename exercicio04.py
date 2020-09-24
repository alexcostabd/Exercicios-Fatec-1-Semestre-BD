## Ao completar o tanque de combustível de um automóvel, faça um algoritmo que
## calcule o consumo efetuado, assim como a autonomia que o carro ainda teria antes do
## abastecimento. Considere que o veículo sempre seja abastecido até encher o tanque e
## que são fornecidas apenas a capacidade do tanque, a quantidade de litros abastecidos e a
## quilometragem percorrida desde o último abastecimento.
## Adendo;14Km percorridos consome 1 litro de combustivél.

km = 14
capacidade_tanque = float(input("Capacidade do tanque do veiculo: "))
quantidade_abastecida = float(input("Quantidade abasteciada: "))
while True:
    resposta = input("O que deseja consultar:\n1 - consumo\n2 - autonomia\nInsira Sua Opção: ")
    if resposta =="1":
        quantidade_atual = float(input("Quantidade atual de combustivel: "))
        while quantidade_atual > capacidade_tanque:
            print("Ops, Consumo maior que capacidade. Verifique a quantidade atual de combustivel!")
            quantidade_atual = float(input("Quantidade atual de combustivel: "))
        consumo_efetuado = capacidade_tanque - quantidade_atual
        print("O consumo atual é de {:.2f} Litros de Combustivel.\nVocê Percorreu {:.2f}Km até o momento".format(consumo_efetuado, consumo_efetuado * km))
    elif resposta =="2":
        quantidade_atual = float(input("Quantidade atual de combustivel: "))
        print("Você ainda pode percorrer {:.2f}Km".format(quantidade_atual*km))
    else:
        print("Ops, ocorreu algum problema, tente novamente!")
    
    continua = input("deseja realizar outra consulta?\n1 - SIM\n2 - NÃO\nDigite: ")
    if continua =="2": break


