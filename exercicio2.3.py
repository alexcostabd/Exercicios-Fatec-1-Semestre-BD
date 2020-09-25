## Desenvolva um algoritmo que calcule as raízes de uma equação do 2º grau, na forma
## Ax2 + Bx + C, levando em consideração a existência de raízes reais.
import math

def deltaRaiz(A, B, C):
    delta = math.pow(B, 2) - 4 * A * C
    return delta

def recebeValoresFuncao():
    A = int(input("Insira o valor de A: "))
    B = int(input("Insira o valor de B: "))
    C = int(input("Insira o valor de C: "))    
    return A, B, C

def calculaRaizaes(delta, A, B):
    if delta == 0:
        x1 = (-B + math.sqrt(delta)) // 2 * A
        return x1
    else:
        x1 = (-(B) - math.sqrt(delta)) // 2 * A
        x2 = (-(B) + math.sqrt(delta)) // 2 * A
        return x1, x2

def main():    
    A,B,C = recebeValoresFuncao()
    print("Equação a ser calculada: {}x^2 {}x {}".format(A, B, C))

    delta = deltaRaiz(A,B,C)
    if delta < 0:
        print("Nenhuma raiz real: quando delta é menor que zero. (negativo)")

    else: ##Uma única raiz real: quando delta for igual a zero. (nulo)
        resultado = calculaRaizaes(delta, A, B)
       
        if delta > 0:        
            print("x'= {}, x\"= {} ".format(resultado[0],resultado[1]))
        else:
            print("x'= {} ".format(resultado))
    
if __name__ == "__main__":
    main()


