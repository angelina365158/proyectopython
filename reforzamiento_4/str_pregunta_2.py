"""Ejercicio 2: contar cuántas veces aparece cada vocal"""

frase = "Programación en Python".lower()
vocales = "aeiou"

for vocal in vocales:
    print(f"{vocal}: {frase.count(vocal)}")