## Faça um algoritmo que leia o ano de nascimento de uma pessoa, calcule e mostre sua idade
# e, também, verifique e mostre se ela já tem idade para votar ( 16 anos ou mais) e para
# conseguir a Carteira de Habilitação ( 18 anos ou mais).
from datetime import datetime
dia_nascimento, mes_nascimento, ano_nascimento = input("Insira sua data de Nasciemnto ex.:(01/01/2000): ").strip().split("/")
now = datetime.now()
dia_atual = now.day
mes_atual = now.month
ano_atual = now.year

if int(mes_nascimento) > mes_atual:##Ainda não completou mais um ano        
    idade = ano_atual - int(ano_nascimento) - 1
    if idade >= 16 and idade < 18:        
        print("sua idade é de {} anos, e você já tem idade para votar".format(idade))
    elif idade >= 18:
        print("sua idade é de {} anos, e você já tem idade para votar e dirigir".format(idade))
else:
    idade = ano_atual - int(ano_nascimento)
    if idade >= 16 and idade < 18:        
        print("sua idade é de {} anos, e você já tem idade para votar".format(idade))
    elif idade >= 18:
        print("sua idade é de {} anos, e você já tem idade para votar e dirigir".format(idade))

