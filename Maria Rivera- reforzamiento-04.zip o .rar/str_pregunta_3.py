"""Ejercicio 3: buscar palabra sin importar mayúsculas o minúsculas"""

frase = input("Ingrese una frase: ")
palabra = input("Ingrese la palabra a buscar: ")

posicion = frase.lower().find(palabra.lower())

if posicion != -1:
    print(f"{palabra} aparece en la posición {posicion}")
else:
    print("La palabra no aparece en la frase.")