"""Ejercicio 2: mostrar cuadrados entre dos números"""

def cuadrados(a, b):
    for i in range(a, b + 1):
        print(i ** 2, end=" ")

x = int(input("Ingrese primer número: "))
y = int(input("Ingrese segundo número: "))

cuadrados(x,y)