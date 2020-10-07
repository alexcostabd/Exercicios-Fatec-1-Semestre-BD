##Tendo como dados de entrada a altura e o sexo de uma pessoa, construa um algoritmo que
#calcule seu peso ideal, utilizando as seguintes fórmulas:
# para homens: (72.7 * h)- 58; 
# para mulheres: (62.1 * h) - 44.7
def recebePessoa():    
    pessoa = str(input("Digite [ H ] para homem e [ M ] para mulher: ")).strip().upper()[0]
    altura = float(input("Didite sua altura ex.:(1.70): "))
    return pessoa, altura

def calculaImcMulher(altura):
    return (62.1 * altura) - 44.7

def calculaImcHomen(altura):
    return (72.7 * altura)- 58;


def main():
    escolha = recebePessoa()
    if escolha[0] == "M":
        print("Seu peso ideal é: {:.2f} Kg".format(calculaImcMulher(escolha[1])))
    else:
        print("Seu peso ideal é: {:.2f} Kg".format(calculaImcHomen(escolha[1])))

if __name__ == "__main__":
    main()
