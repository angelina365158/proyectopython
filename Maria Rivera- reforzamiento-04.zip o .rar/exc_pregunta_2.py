"""Ejercicio 2 - Excepciones
Crear una función que maneje excepciones de tipo IndexError y TypeError.
- Solo acepta datos enteros.
- Si el índice está fuera de rango, debe avisar al usuario.
- Usar la función al menos 3 veces, incluyendo un caso de error"""

lista = [2, 6, 10, 4, 5, 23, 1]

def insertar_valor_en_lista(lista, indice, valor):
    try:
        # Validar que el valor sea entero
        if not isinstance(valor, int):
            raise TypeError("El valor ingresado no es un entero.")

        # Intentar asignar el valor en el índice dado
        lista[indice] = valor
        print(f"Valor {valor} insertado correctamente en la posición {indice}.")
        print("Lista actualizada:", lista)

    except TypeError as te:
        print(f"Error de tipo: {te} | Solución: Ingrese un número entero.")

    except IndexError:
        print(f"Error: El índice {indice} está fuera de rango.")
        print(f"Rango permitido: 0 a {len(lista)-1}")

    finally:
        print("Operación finalizada.\n")


# Probar la función

# Caso 1: Correcto
insertar_valor_en_lista(lista, 2, 50)
# Actualiza el índice 2 con valor 50

# Caso 2: Índice fuera de rango
insertar_valor_en_lista(lista, 10, 30)
# Error por índice fuera de rango

# Caso 3: Tipo de dato incorrecto
insertar_valor_en_lista(lista, 3, "texto")
# Error por valor no entero