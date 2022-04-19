"""PROGRAMA PARA INVERTIR UN NUMERO CON CUATRO DIGITOS"""

print("-----------------------------------------------")
print("---- INVERSION DE NUMERO CON 4 DIGITOS --------")
print("-----------------------------------------------")

#Input
a = input ("Ingrese un numero de 4 cifras: ")
a = int (a)


#Processing
x = a%10
y = int((a%100)/10)
m = int((a%1000)/100)
n = int((a -(a%1000))/1000)

#Output
print("El inverso de este numero es: " + str(x+y+m+n))