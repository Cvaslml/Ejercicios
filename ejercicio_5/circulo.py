"""PROGRAMA PARA CALCULAR EL AREA Y PERIMETRO DE UN CIRCULO"""

import math


print("------------------------------------------")
print("---- AREA Y PERIMETRO DEL CIRCULO --------")
print("------------------------------------------")

#Input
r = input ("Introduzca el valor del radio del circulo: ")
r = int (r)


#Processing
a = math.pi*r^2
p = math.pi*2*r

#Output
print("El area del circulo es: " + str(a), "Y el perimetro del circulo es: " + str(p))