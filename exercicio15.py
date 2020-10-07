#O IMC - lndice de Massa Corporal é um critério da Organização Mundial de Saúde para
#dar uma indicação sobre a condição de peso de uma pessoa adulta. A fórmula é IMC =
#peso/ (altura)2
#• Elabore um algoritmo que leia o peso e a altura de um adulto e mostre sua
#condição. 

def condicao(indice):
    if indice < 18.5: return "Abaixo do Peso"
    elif 18.5 <= indice < 25: return "Peso normal"
    elif 25 <= indice < 30: return "Acima do Peso"
    elif indice >= 30: return "Obeso"

def main():
    peso = float(input("Insira seu Peso: "))
    altura = float(input("Insira sua Altura: "))
    imcIndice =  peso // pow(altura, 2)
    print(condicao(imcIndice))


if __name__ == "__main__":
    main()