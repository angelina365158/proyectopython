"""
Requisitos:

1. Crear 2 variables enteras, 2 variables flotantes, 2 variables string, 1 variable string que contiene
valor numérico y una variable boolean
2. Obtener y mostrar la suma de una variable entera con la variable numérica.
3. Obtener y mostrar la suma de las 2 variables enteras más la variable string numérica
 y la variable flotante
 4. Obtener y mostrar el módulo de las variables enteras: %
 5. Obtener y mostrar el resultado de la parte entera de los variables enteras: //
6. Obtener una potencia usando una de las variables flotantes y
 la variable entera como potencia
"""
var_entero_1=13
var_entero_2=22
var_float_1=30.6
var_float_2=40.8
nombre="Maria"
apellido="Rivera"
var_string="1010"
var_boolean=False

suma_1=var_entero_1+int(var_string)
suma_2=var_entero_1+var_entero_2+int(var_string)+var_float_1
modulo_1=var_entero_2%var_entero_1
parte_entera=var_entero_2//var_entero_1
potencia=pow(var_float_1,var_entero_2)

print(f"Solucion 1: {suma_1}")
print(f"Solucion 2: {suma_2}")
print(f"Solucion 3: {modulo_1}")
print(f"Solucion 4: {parte_entera}")
print(f"Solucion 5: {potencia}")







