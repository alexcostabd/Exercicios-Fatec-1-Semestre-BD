##Construa um algoritmo que calcule a média ponderada entre 5 números quaisquer, sendo
##que os pesos a serem aplicados são 1, 2, 3, 4 e 5 respectivamente.

a,b,c,d,e = str(input("Insira os cinco valores: ")).strip().split(" ")
mediaPonderada = ((int(a) * 1) + (int(b) * 2) + (int(c) * 3)  + (int(d) * 4) + (int(e) * 5))
print("Média ponderada dos valores: {:.2f}".format(mediaPonderada))

