"""Crear una clase Persona que contenga dos atributos: nombre y edad.
Nombre y edad se ingresarán por teclado en el constructor"""

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad


class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self.sueldo = sueldo

    def calcular_impuesto(self):
        if self.sueldo > 4000:
            impuesto = self.sueldo * 0.10
            return f"{self.nombre} debe pagar S/ {impuesto:.2f} de impuestos."
        else:
            return f"{self.nombre} no debe pagar impuestos."


# Instancias
empleado1 = Empleado("Lucía", 29, 3800)
empleado2 = Empleado("Pedro", 35, 5000)
empleado3 = Empleado("Ana", 41, 4500)

print(empleado1.calcular_impuesto())
print(empleado2.calcular_impuesto())
print(empleado3.calcular_impuesto())