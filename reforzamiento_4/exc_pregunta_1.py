"""Ejercicio 1: división segura con validación"""

def division_segura(a, b):
    try:
        a = float(a)
        b = float(b)
        print("Resultado:", a / b)
    except ZeroDivisionError:
        print("Error: no puedes dividir entre cero")
    except ValueError:
        print("Error: Entrada no numérica")
    finally:
        print("Operación finalizada")

division_segura(10, 2)
division_segura(8, 0)
division_segura("x", 3)
