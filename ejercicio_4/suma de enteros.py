"""PROGRAMA PARA DETERMINAR LA SUMATORIA DE LOS PRIMERO N ENTEROS POSITIVOS"""


print("----------------------------------------------")
print("---- SUMATORIA DE N ENTEROS POSITIVOS --------")
print("----------------------------------------------")

#Input
N = input ("Ingresa el valor de N: ")
N = int (N)

#Processing
s = N(N+1)/2

#Output
print("La sumatoria de numeros desde 1 hasta: " + str(N), "es: " + str(s))