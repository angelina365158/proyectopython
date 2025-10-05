"""Crear un decorador conteo_parametros(funcion) donde imprimirá la
cantidad de argumentos que tiene la función a decorar usando *args y
**kwargs"""
#Decorador
def conteo_parametros(funcion):
    def wrapper(*args, **kwargs):
        total_args = len(args) + len(kwargs)
        print(f"La cantidad de argumentos que tiene la función es {total_args}")

        #Verificar que todos los parámetros sean enteros
        for valor in list(args) + list(kwargs.values()):
            if not isinstance(valor, int):
                print("Solo está admitido datos enteros, no se podrá realizar la suma\n")
                return None

        #Ejecutar la función original
        resultado = funcion(*args, **kwargs)

        print("La función decoradora terminó de ejecutarse correctamente\n")
        return resultado
    return wrapper

#Función a decorar
@conteo_parametros
def suma(*args, **kwargs):
    total = sum(args) + sum(kwargs.values())
    print(f"La suma de los números es: {total}")
    return total

#Usar la función decorada al menos 3 veces
suma(4, 1, 10, 2, 50, 64)
suma(5, 10, x=15, y=20)  # mezcla de args y kwargs
suma(3, "hola", 7)       # caso con string (error)