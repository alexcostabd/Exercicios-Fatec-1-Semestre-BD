##Escreva um algoritmo que leia o código de um determinado produto e mostre a sua
#classificação.

codigo = int(input("Insira o código do prosuto: "))
if codigo == 1:
    print("Alimento não-perecível ")
elif 2 <=  codigo <= 4:
    print("Alimento perecível")
elif 5 <= codigo <= 7:
    print("Vestuário")
elif codigo == 7:
    print("Higiene pessoal")
elif 8 <= codigo <= 15:
    print("Limpeza e utensílios domésticos")
else:
    print("Inválido")
    
   