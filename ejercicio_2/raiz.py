"""PROGRAMA PARA CALCULAR LA RAIZ CON SU INDICE"""

print("-----------------------------------")
print("----RESULTADO DE LA RAIZ DADA--------")
print("-----------------------------------")

#Input
x = input ("Valor del radicando: ")
x = int (x)
y = input ("valor del indice de la raiz: ")
y = int (y)

#Processing
z = y**(1/x)

#Output
print("El valor de la raiz es: " + str(z))