"""Ejercicio 3 - Excepciones
Crear la función funciona_indice(persona, indice) que valide:
- Si el índice existe en el diccionario.
- Si el índice ingresado es de tipo string.
- Si ocurre algún error, mostrar mensajes personalizados"""

# Diccionario base
persona = {'nombre': 'Xavier','apellido': 'Rodriguez','dni': '63325345'}

def funciona_indice(persona, indice):
    try:
        # Validar que el índice sea string
        if not isinstance(indice, str):
            raise TypeError("El índice debe ser una cadena de texto (string).")

        # Intentar acceder al índice en el diccionario
        valor = persona[indice]
        print(f"El valor de '{indice}' es: {valor}")

    except KeyError:
        print(f"Error: El índice '{indice}' ingresado no existe en el diccionario.")
        print(f"Claves disponibles: {list(persona.keys())}")

    except TypeError as te:
        print(f"Error de tipo: {te} | Solución: Ingrese un texto como clave.")

    finally:
        print("Operación finalizada.\n")


# Probar la función

# Caso 1: Acceso correcto
funciona_indice(persona, 'nombre')

# Caso 2: Índice inexistente
funciona_indice(persona, 'profesion')

# Caso 3: Tipo de dato incorrecto
funciona_indice(persona, 123)