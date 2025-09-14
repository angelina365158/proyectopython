"""
Operador comunes
Operador Suma
"""

var_1 = "7000"
var_2 = 47333
var_3 = 56.9

suma_1 = int(var_1) + var_2
print(suma_1)


nombre = "Johanna"
apellido = "Gutierrez"
nombre_completo = nombre + " " +apellido
print(nombre_completo)

print("________________________________")
suma_2 = str(var_2) + var_1
print(suma_2)
print("Tipo de dato: {}".format(type(suma_2)))

print("________________________________")
suma_3 = var_2 + var_3
print(suma_3)

print("________________________________")
suma_4 = var_1 + str(var_2) + str(var_3)
print(suma_4)
print("Tipo de dato: {}".format(type(suma_4)))
