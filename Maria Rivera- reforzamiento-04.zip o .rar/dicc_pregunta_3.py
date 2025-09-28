"""Parte 3: convertir diccionario a lista y mostrar el tipo final"""

persona = {"nombre":"Maria","salario":1600,"dni":"60732970"}

lista_persona = list(persona.items())
print("Lista resultante:", lista_persona)
print("Tipo final:", type(lista_persona))