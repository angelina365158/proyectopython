"""
Conversión de datos
"""

var_str = "58547552"
nombre = "Johanna"
modulo = 2
prom = 18.9

#Conversión de string a int
var_int = int(var_str)
print(var_int)
print("Tipo de dato: {}".format(type(var_int)))

#Conversión de entero a string
var_mod =  str(modulo)
print(var_mod)
print("Tipo de dato: {}".format(type(var_mod)))

#Conversión de string a int (no es posible)
#var_nom = int(nombre)
#print(type(var_nom))

#conversión de flotante a entero
var_int = int(prom)
print(var_int)
print("Tipo de dato: {}".format(type(var_int)))
