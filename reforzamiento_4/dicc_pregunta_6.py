"""Ejercicio 6: crear diccionario con 4 números como keys y sus cubos como valores"""

numeros = {}
for i in range(4):
    num = int(input(f"Ingrese el número {i+1}: "))
    numeros[num] = num ** 3

print("Diccionario final:", numeros)