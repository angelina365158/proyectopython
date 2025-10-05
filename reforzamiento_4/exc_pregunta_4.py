"""Ejercicio 4 - Excepciones
Crear la función saluda_fecha(nombre, dia, mes, anio) que valide:
- El nombre NO puede ser un número
- Día, mes y año NO pueden ser cadenas de texto
- Siempre debe mostrar "Operación finalizada" con finally"""

def saluda_fecha(nombre, dia, mes, anio):
    try:
        # Validar que el nombre no sea numérico
        if nombre.isnumeric():
            raise ValueError("El nombre no puede ser numérico. Por favor, ingrese un nombre válido.")

        # Validar que dia, mes y anio sean números
        if not isinstance(dia, int) or not isinstance(mes, str) or not isinstance(anio, int):
            raise TypeError("Día y año deben ser enteros, mientras que mes debe ser texto (string).")

        # Si todo es correcto, mostrar mensaje
        cadena = f"Hello {nombre}, hoy estamos {dia:02d} de {mes} del {anio}"
        print(cadena)

    except ValueError as ve:
        print(f"Error de valor: {ve}")

    except TypeError as te:
        print(f"Error de tipo: {te}")

    finally:
        print("Operación finalizada.\n")


# Probar la función

# Caso 1: Datos correctos
saluda_fecha("Leonardo", 4, "agosto", 2025)

# Caso 2: Nombre numérico
saluda_fecha("12345", 10, "setiembre", 2024)

# Caso 3: Día incorrecto (tipo string en lugar de int)
saluda_fecha("María", "10", "julio", 2023)