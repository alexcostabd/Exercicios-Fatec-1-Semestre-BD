## Escreva um algoritmo que, a partir de um mês fornecido (número inteiro de 1 a 12),
## apresente o nome dele por extenso ou uma mensagem de mês inválido. 

mes = ["Janeiro", "Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"]

while True:
    mes_escolhido = int(input("Insira um valor de 1 a 12: "))
    while mes_escolhido <= 0 or mes_escolhido >=13:
        print("Insira um valor válido!")
        mes_escolhido = int(input("Insira um valor de 1 a 12: "))
    print("O mês selecionado foi {}".format(mes[mes_escolhido-1]))

    continuar = int(input("Deseja continuar[1 - SIM e 2 - Não]: "))
    if continuar != 1: break;


