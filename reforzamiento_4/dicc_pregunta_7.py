"""Ejercicio 7: alumnos y notas en un diccionario, lueg mostrar cada alumno con su nota y la media"""

alumnos = {}
n = int(input("Ingrese la cantidad de alumnos: "))

for i in range(n):
    nombre = input(f"Ingrese el nombre del alumno {i+1}: ")
    nota = float(input(f"Ingrese la nota de {nombre}: "))
    alumnos[nombre] = nota

# Mostrar alumnos y notas
suma_notas = 0
for nombre, nota in alumnos.items():
    print(f"{nombre} tiene la nota de {nota}")
    suma_notas += nota

media = suma_notas / n
print("La media de las notas es:", media)