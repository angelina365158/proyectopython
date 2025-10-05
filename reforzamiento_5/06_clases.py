"""Desarrolla una clase Agenda que administrará contactos"""

class Agenda:
    def __init__(self):
        self.contactos = []

    def agregar_contacto(self, nombre, telefono, email, dni):
        contacto = {'nombre': nombre,'telefono': telefono,'email': email,'dni': dni}
        self.contactos.append(contacto)
        print(f"Contacto {nombre} agregado correctamente.")

    def mostrar_contactos(self):
        print("\n--- Lista de Contactos ---")
        for c in self.contactos:
            print(f"Nombre: {c['nombre']}, Teléfono: {c['telefono']}, Email: {c['email']}, DNI: {c['dni']}")

    def buscar_contacto(self, dni):
        for c in self.contactos:
            if c['dni'] == dni:
                print(f"\nContacto encontrado: {c['nombre']} - Tel: {c['telefono']}")
                return
        print(f"\nEl contacto con DNI {dni} no se encuentra en la agenda.")


#Instancia de la clase Agenda
agenda = Agenda()
agenda.agregar_contacto("Luis", "997667945", "luishh@gmail.com", 44234239)
agenda.agregar_contacto("Milagros", "997654687", "milagros19c@gmail.com", 43423211)
agenda.agregar_contacto("Raquel", "912345678", "raquel@gmail.com", 42678123)
agenda.agregar_contacto("Carlos", "998877665", "carlosm@gmail.com", 40123456)

agenda.mostrar_contactos()
agenda.buscar_contacto(43423211)  # Existe
agenda.buscar_contacto(44556677)  # No existe