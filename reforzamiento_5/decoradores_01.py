"""Crear una función decoradora que dará los buenos días antes de
ejecutar una función llamada saludo_inicial(nombre) a ser decorada
“Buenos días NOMBRE son las HORA horas con MINUTOS minutos” y
luego de ser ejecutada lanzará un mensaje diciendo “Hasta luego
NOMBRE que tenga buen día”"""

from datetime import datetime

#Decorador
def buenos_dias(func):
    def wrapper(nombre):
        hora_actual = datetime.now()
        hora = hora_actual.hour
        minutos = hora_actual.minute

        #Mensaje antes de ejecutar la función
        print(f"Buenos días {nombre}, son las {hora} horas con {minutos} minutos.")

        #Ejecutar la función decorada
        mensaje = func(nombre)

        #Mensaje después de la función
        print(f"Hasta luego {nombre}, que tenga buen día.\n")

        return mensaje
    return wrapper

#Función a decorar
@buenos_dias
def saludo_inicial(nombre):
    return f"¡Hola {nombre}! Bienvenido/a."

#Usar la función decorada al menos 3 veces
print(saludo_inicial("Raquel"))
print(saludo_inicial("Carlos"))
print(saludo_inicial("Lucía"))