"""Ejercicio 3: sumar dígitos de un número"""

def sumar_digitos(num):
    return sum(int(d) for d in str(num))

numero = int(input("Ingrese un número: "))
print("Suma de los dígitos:", sumar_digitos(numero))