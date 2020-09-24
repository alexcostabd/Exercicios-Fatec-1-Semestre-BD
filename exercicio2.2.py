## 2.2 Escreva um algoritmo que leia três valores inteiros e diferentes e mostre-os em ordem
## decrescente. Utilize para tal uma seleção encadeada.

## Solicita os valores via terminal
valor01 = int(input("1º Valor: "))
valor02 = int(input("2º Valor: "))
valor03 = int(input("3º Valor: "))

## Verifica se existe valores iguais
if valor01 != valor02 and valor01 != valor03 and valor02 != valor03:
    menor = valor01
    meio = 0
    maior = 0
    if valor02 < valor01 and valor02 < valor03:
        if valor03 < valor01:            
            menor = valor02
            meio = valor03
            maior = valor01        
        else:
            menor = valor02
            meio = valor01
            maior = valor03
        
    elif valor03 < valor01 and valor03 < valor02:
        if valor02 < valor01:            
            menor = valor03
            meio = valor02
            maior = valor01        
        else:
            menor = valor03
            meio = valor01
            maior = valor02
    print("{} - {} - {}".format(maior, meio, menor))
else:
   print("Existem valores iguais...")

    

        
    
    
