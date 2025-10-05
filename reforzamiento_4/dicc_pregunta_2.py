"""Parte 2: agregar clave "dni", mostrar salario y dni, luego eliminar edad"""

persona = {"nombre": "Maria","edad": 31,"salario": 1600}

# Agregar nuevo key
persona["dni"] = "60732970"

# Mostrar salario y dni
print("Salario:", persona["salario"])
print("DNI:", persona["dni"])

# Eliminar edad
del persona["edad"]

# Mostrar diccionario actualizado
print("Diccionario actualizado:", persona)