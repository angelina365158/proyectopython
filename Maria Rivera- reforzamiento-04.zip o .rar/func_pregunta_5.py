"""Ejercicio 5: eliminar valor de lista"""

def eliminar_valor(lista, valor):
    print("Lista original:", lista)
    if valor in lista:
        lista.remove(valor)
    return lista

lista_usuario = [int(x) for x in input("Ingrese valores separados por espacio: ").split()]
valor_eliminar = int(input("Ingrese el valor a eliminar: "))

lista_actualizada = eliminar_valor(lista_usuario, valor_eliminar)
print("Lista actualizada:", lista_actualizada)