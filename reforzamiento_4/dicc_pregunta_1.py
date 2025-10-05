"""Parte 1: crear un diccionario con nombre, edad, salario y edad,
luego convertir el diccionario a lista"""

persona = {"nombre": "Maria","edad": 31,"salario": 1600}

# Convertir a lista
lista_persona = list(persona.items())
print("Diccionario como lista:", lista_persona)