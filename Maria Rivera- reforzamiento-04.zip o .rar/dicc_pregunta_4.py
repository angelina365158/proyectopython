"""Ejercicio 4: Diccionario con 6 departamentos, borrar uno, actualizar penúltimo y verificar"""

departamentos = {1: "Lima",2: "Cusco",3: "Arequipa",4: "Huanuco",5: "Junín",6: "Loreto"}

# Borrar un departamento
del departamentos[2]

# Actualizar el penúltimo departamento
departamentos[5] = "Huancayo"

# Comprobar si Cusco existe
print("¿'Cusco' en valores?", "Cusco" in departamentos.values())

print("Diccionario final:", departamentos)