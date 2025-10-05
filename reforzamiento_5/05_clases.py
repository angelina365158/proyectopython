"""Crear una clase PersonaPrestamo que hereda de la clase anterior (problema 4) donde tendrá los métodos"""


class Persona:
    def __init__(self, nombre, edad, meses_trabajando, sueldo):
        self.nombre = nombre
        self.edad = edad
        self.meses_trabajando = meses_trabajando
        self.sueldo = sueldo

    def mostrar_datos(self):
        return {"Nombre": self.nombre,"Edad": self.edad,"Meses trabajando": self.meses_trabajando,"Sueldo": self.sueldo}

# Clase del problema 6 que hereda de Persona
class PersonaPrestamo(Persona):

    # Metodo para verificar si está apta para préstamo
    def apto_para_prestamo(self):
        if self.meses_trabajando > 12 and self.edad > 25:
            return f"{self.nombre} está apto(a) para un préstamo."
        else:
            return f"{self.nombre} NO está apto(a) para un préstamo."

    # Metodo para calcular el préstamo si está aprobado
    def calcular_prestamo(self):
        if self.meses_trabajando > 12 and self.edad > 25:
            cantidad_prestamo = self.sueldo * 10
            return f"{self.nombre} recibirá un préstamo de {cantidad_prestamo} soles."
        else:
            return f"{self.nombre} no cumple con los requisitos para recibir un préstamo."

# Instanciando 3 personas con diferentes casos
persona1 = PersonaPrestamo("Carlos", 30, 24, 1500)
persona2 = PersonaPrestamo("Ana", 22, 18, 1800)
persona3 = PersonaPrestamo("Luis", 40, 10, 2000)

# Mostramos resultados
for persona in [persona1, persona2, persona3]:
    print(persona.mostrar_datos())
    print(persona.apto_para_prestamo())
    print(persona.calcular_prestamo())
    print("-" * 50)