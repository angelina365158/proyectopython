"""Haciendo el uso de *args y **kwargs aplicarlo debidamente para
decorar una función que recibirá 6 argumentos los cuales se
multiplicarán entre ellos (3 de ellos serán usado con **kwargs)"""

#Decorador
def ejecutar_funcion(func):
    def wrapper(*args, **kwargs):
        print("Está por ejecutarse la función")

        #Ejecutar la función original con los argumentos recibidos
        resultado = func(*args, **kwargs)

        print("La función ha sido ejecutado correctamente\n")
        return resultado
    return wrapper


#Función a decorar
@ejecutar_funcion
def multiplicar_numeros(a, b, c, **kwargs):
    #Extraer los valores de **kwargs
    d = kwargs.get('d', 1)
    e = kwargs.get('e', 1)
    f = kwargs.get('f', 1)

    #Multiplicar los 6 valores
    resultado = a * b * c * d * e * f
    print(f"El resultado de multiplicar los números es: {resultado}")
    return resultado


#Usar la función decorada al menos 3 veces
multiplicar_numeros(2, 3, 4, d=5, e=6, f=7)
multiplicar_numeros(1, 2, 3, d=4, e=5, f=6)
multiplicar_numeros(3, 3, 3, d=3, e=3, f=3)