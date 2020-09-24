##Prepare um algoritmo capaz de inverter um número, de 3 dígitos, fornecido, ou seja,
##apresentar primeiro a unidade e, depois, a dezena e a centena.

num = input("Insira o Valor a ser invertido: ").strip()
print("O valor invertido é {}".format(num[::-1]))