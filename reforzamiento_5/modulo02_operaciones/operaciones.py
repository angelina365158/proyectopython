#Para operaciones
def cargar_numeros():
    numeros = []
    for i in range(3):
        num = int(input(f"Ingrese el número {i+1}: "))
        numeros.append(num)
    return numeros

def calcular_media(numeros):
    return sum(numeros) / len(numeros)

def numero_mayor(numeros):
    return max(numeros)