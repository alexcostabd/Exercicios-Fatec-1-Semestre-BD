# Elabore um algoritmo que leia o valor de dois números inteiros e a operação aritmética
# desejada; calcule, então, a resposta adequada. Utilize os símbolos da tabela a seguir para ler
# qual a operação aritmética escolhida. 

x = int(input("Insira o primeiro valor: "))
y = int(input("Insira o segundo valor: "))
operacao = input("Selecione a operações [+, -, /, *]: ").strip()

if operacao == "+":
    print("Valor da soma dos valores é: {}".format(x + y))
elif operacao == "*":
    print("Valor da multiplicação dos valores é: {}".format(x * y))
elif operacao == "/":
    print("Valor da multiplicação dos valores é: {}".format(x // y))
else:
    if x > y:
        print("Valor da subtração dos valores é: {}".format(x - y))
    else:
        print("Valor da subtração dos valores é: {}".format(y - x))

