## Elabore um algoritmo que, a partir de um dia, mês e ano fornecidos, valide se eles
# compõem uma data válida. Não deixe de considerar os meses com 30 ou 31 dias, e o
# tratamento de ano bissexto.

def verificaMes(valMes):
    if valMes == 2:
        return 0
    elif valMes == 4 or valMes == 6 or valMes == 9 or valMes == 11:
        return 1
    else:
        return 2


def verificaAnoBissexto(ano):
    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
        return True
    else:
        return False


def printRetorno(valor):
    if valor:
        print("Data válida, ano é Bissexto!")
    else:
        print("Data válida, ano não é Bissexto! ")


def main():
    dia, mes, ano = input("Insira sua data de nascimento ex.: 01/01/1900: ").strip().split('/')
    ret = verificaMes(int(mes))
    if ret == 0:
        retAno = verificaAnoBissexto(int(ano))
        if retAno and int(dia) <= 29:
            printRetorno(retAno)
        elif not retAno and int(dia) <= 28:
            printRetorno(retAno)
        else:
            print("Data inválida!")
    elif ret == 1 and int(dia) <= 30:
        retAno = verificaAnoBissexto(int(ano))
        printRetorno(retAno)

    elif ret == 2 and int(dia) <= 31:
        retAno = verificaAnoBissexto(int(ano))
        printRetorno(retAno)
    else:
        print("Data inválida!")


if __name__ == '__main__':
    main()
