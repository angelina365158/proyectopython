"""Crear una clase Empleado"""
#pida ingresar un nombre, apellido y edad
class Empleado:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.sueldo = 0
#sueldo
    def ingresar_sueldo(self):
        self.sueldo = float(input(f"Ingrese el sueldo actual de {self.nombre} {self.apellido}: "))
#comprimir
    def mostrar_datos(self):
        datos = {"Nombre": self.nombre,"Apellido": self.apellido,"Edad": self.edad,"Sueldo": self.sueldo}
        print(datos)


#Instanciación de 3 empleados
empleado1 = Empleado("Carlos", "Pérez", 30)
empleado2 = Empleado("María", "López", 25)
empleado3 = Empleado("José", "Ramírez", 40)

#Asignar sueldos (puedes usar input o directamente asignar)
empleado1.sueldo = 2500
empleado2.sueldo = 3100
empleado3.sueldo = 4000

#Mostrar resultados
empleado1.mostrar_datos()
empleado2.mostrar_datos()
empleado3.mostrar_datos()