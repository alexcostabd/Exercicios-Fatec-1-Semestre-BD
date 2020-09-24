## Dada uma determinada data de aniversário (dia, mês e ano separadamente), elabore um
## algoritmo que solicite a data atual (dia, mês e ano separadamente) e calcule a idade em
## anos, em meses e em dias.

dia_nascimento, mes_nascimento, ano_nascimento = input("Insira seu dia, mes e ano de nascimento ex.:(01/01/2000): ").strip().split("/")
dia_atual, mes_atual, ano_atual = input("Insira seu dia, mes e ano de atual ex.:(01/01/2020): ").strip().split("/")

if int(mes_nascimento) > int(mes_atual):##Ainda não completou mais um ano        
    anos = ((int(ano_atual) - int(ano_nascimento)) - 1)
    meses = anos * 12
    dias = meses * 30 + int(dia_atual)
    print("sua idade é de {} anos, {} meses e {} dias".format(anos,meses,dias))
else:
    anos = (int(ano_atual) - int(ano_nascimento))
    meses = anos * 12
    dias = meses * 30 + int(dia_atual)
    print("sua idade é de {} anos, {} meses e {} dias".format(anos,meses,dias))
        
    
