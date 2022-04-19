"""PROGRAMA PARA CALCULAR EL IVA Y 
 PRECIO DE VENTA DE UN PRODUCTO"""

print("-----------------------------------")
print("---- IVA Y PRECIO DE VENTA --------")
print("-----------------------------------")

#Input
x = input ("Valor del producto: $ ")
x = int (x)
y = input ("Porcentaje del iva en decimal: ")
y = float (y)

#Processing
iva = x * y
ptotal = x + iva

#Output
print("El iva de su producto es: $" + str(iva), "precio total: $" + str(ptotal))