"""Ejercicio 1: número cuya suma de dígitos sea mayor y mostrar menores a 10"""

def suma_digitos(num):
    return sum(int(d) for d in str(num))

num1 = int(input("Ingrese primer número: "))
num2 = int(input("Ingrese segundo número: "))

if suma_digitos(num1) > suma_digitos(num2):
    print("Número con suma mayor:", num1)
else:
    print("Número con suma mayor:", num2)

for num in [num1, num2]:
    if suma_digitos(num) < 10:
        print(f"{num} tiene sumatoria menor a 10")