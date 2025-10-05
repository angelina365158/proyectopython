"""Crear una clase Persona con los siguientes requerimientos"""

class Persona:
    def __init__(self, nombre, edad, sueldo):
        self.nombre = nombre
        self.edad = edad
        self.sueldo = sueldo

    def mostrar_datos(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, Sueldo: S/. {self.sueldo}")

    def es_mayor_de_edad(self):
        return self.edad >= 18

    def bonificacion(self):
        if self.es_mayor_de_edad():
            return self.sueldo * 0.20
        else:
            return 0

    def meses_trabajando(self, anios):
        return anios * 12


# Instanciación de 3 personas
persona1 = Persona("Juan", 35, 2500)
persona2 = Persona("Raquel", 17, 1800)
persona3 = Persona("Luis", 28, 3000)

# Mostrar información
for persona in [persona1, persona2, persona3]:
    persona.mostrar_datos()
    print("Mayor de edad:", "Sí" if persona.es_mayor_de_edad() else "No")
    print(f"Bonificación: S/. {persona.bonificacion():.2f}")
    print(f"Meses trabajando (5 años): {persona.meses_trabajando(5)} meses\n")