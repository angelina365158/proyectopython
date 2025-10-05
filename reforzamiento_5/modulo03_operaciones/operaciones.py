#Para operaciones
import random

def generar_lista():
    """Genera 30 números enteros aleatorios entre 0 y 100"""
    lista = [random.randint(0, 100) for _ in range(30)]
    print("Lista generada:")
    print(lista)
    return lista

def ordenar_lista(lista):
    """Ordena los valores de la lista"""
    lista_ordenada = sorted(lista)
    print("\nLista ordenada:")
    print(lista_ordenada)
    return lista_ordenada

def numero_mayor(lista):
    """Devuelve el número mayor de la lista"""
    mayor = max(lista)
    print(f"\nEl número mayor de la lista es: {mayor}")
    return mayor