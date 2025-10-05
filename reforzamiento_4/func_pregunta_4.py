"""Ejercicio 4: comparar cantidad de letras en nombres"""

def contar_letras(nombre):
    return len(nombre.replace(" ", ""))

n1 = input("Ingrese nombre y apellidos de la primera persona: ")
n2 = input("Ingrese nombre y apellidos de la segunda persona: ")

if contar_letras(n1) > contar_letras(n2):
    print(f"{n1} tiene más letras en su nombre.")
else:
    print(f"{n2} tiene más letras en su nombre.")
