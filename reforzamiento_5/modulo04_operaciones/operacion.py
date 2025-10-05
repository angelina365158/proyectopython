#Para operaciones
import math

def cargar_valor():
    """Pide al usuario un número entero y valida que sea numérico"""
    while True:
        valor = input("Ingrese un número entero: ")
        if valor.isdigit() or (valor.startswith('-') and valor[1:].isdigit()):
            return int(valor)
        else:
            print("❌ Error: Debe ingresar solo números enteros.")

def raiz_cuadrada(valor):
    """Muestra la raíz cuadrada del número"""
    if valor < 0:
        print("⚠️ No se puede calcular la raíz cuadrada de un número negativo.")
        return None
    resultado = math.sqrt(valor)
    print(f"La raíz cuadrada de {valor} es: {resultado}")
    return resultado

def potencias(valor):
    """Calcula el valor al cuadrado y al cubo"""
    resultados = {
        "cuadrado": valor ** 2,
        "cubo": valor ** 3
    }
    print(f"El número {valor} al cuadrado es {resultados['cuadrado']} y al cubo es {resultados['cubo']}")
    return resultados