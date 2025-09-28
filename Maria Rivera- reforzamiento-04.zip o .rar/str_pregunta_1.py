"""Ejercicio 1: palabra con más caracteres"""

frase = "La programación en Python es poderosa"
palabras = frase.split()
mayor = max(palabras, key=len)

print(f"{mayor} - {len(mayor)} caracteres")
