##Elabore um algoritmo que calcule a área de um círculo qualquer de raio fornecido.  A = π r²
import math
R = float(input("Insira o valor do raio em metros: "))
print("A área do circulo é: {:.3f}m2".format(math.pi * math.pow(R,2)))