"""Crear una clase llamada Soldado para un juego sobre un mapa la cual
deberá tener como atributos en el constructor posición X y posición Y las
cuales iniciarán en 0, agregar un nombre a este soldado dentro de estos
atributos"""

class Soldado:
    def __init__(self, nombre):
        self.nombre = nombre
        self.pos_x = 0
        self.pos_y = 0
        self.historial = []  # lista donde se guardarán los movimientos

    def caminar_x(self, pasos):
        #Movimiento en eje X
        if pasos < 0:
            #Si el movimiento es hacia atrás, no puede pasar de 0
            if abs(pasos) > self.pos_x:
                self.pos_x = 0
            else:
                self.pos_x += pasos
        else:
            self.pos_x += pasos

        #Guardamos el movimiento
        self.historial.append(f"Se movió {pasos} pasos en eje X. Posición actual X={self.pos_x}")

    def caminar_y(self, pasos):
        #Movimiento en eje Y
        if pasos < 0:
            #Si el movimiento es hacia atrás, no puede pasar de 0
            if abs(pasos) > self.pos_y:
                self.pos_y = 0
            else:
                self.pos_y += pasos
        else:
            self.pos_y += pasos

        #Guardamos el movimiento
        self.historial.append(f"Se movió {pasos} pasos en eje Y. Posición actual Y={self.pos_y}")

    def mostrar_historial(self):
        print(f"\nHistorial de movimientos del soldado {self.nombre}:")
        for movimiento in self.historial:
            print(movimiento)
        print(f"\nPosición final -> X: {self.pos_x}, Y: {self.pos_y}")


#-Ejemplo de uso-
soldado1 = Soldado("Capitán Bravo")

#Realizamos al menos 5 movimientos
soldado1.caminar_x(10)
soldado1.caminar_y(5)
soldado1.caminar_x(-3)
soldado1.caminar_y(-10)
soldado1.caminar_x(7)

#Mostrar historial final
soldado1.mostrar_historial()