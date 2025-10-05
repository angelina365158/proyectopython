"""Crear una clase Alumno que tenga como atributos el nombre, edad y la
nota final del alumno"""

class Alumno:
    def __init__(self, nombre, edad, nota_final):
        self.nombre = nombre
        self.edad = edad
        self.nota_final = nota_final

    def mostrar_datos(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, Nota final: {self.nota_final}")

    def resultado(self):
        if self.nota_final >= 13:
            print(f"{self.nombre} ha aprobado")
        else:
            print(f"{self.nombre} no ha aprobado")


# Instanciación de 4 alumnos
alumno1 = Alumno("Lucia", 18, 15)
alumno2 = Alumno("Andrés", 19, 12)
alumno3 = Alumno("Maria", 20, 17)
alumno4 = Alumno("Miguel", 21, 10)

# Mostrar resultados
for alumno in [alumno1, alumno2, alumno3, alumno4]:
    alumno.mostrar_datos()
    alumno.resultado()