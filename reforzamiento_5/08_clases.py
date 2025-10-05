"""Escribir una clase Figura que debe tener un atributo de nombre de la
figura"""

import math

class Figura:
    def __init__(self, nombre):
        self.nombre = nombre


class Rectangulo(Figura):
    def __init__(self, base, altura):
        super().__init__("Rectángulo")
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)


class Circulo(Figura):
    def __init__(self, radio):
        super().__init__("Círculo")
        self.radio = radio

    def area(self):
        return math.pi * self.radio ** 2

    def perimetro(self):
        return 2 * math.pi * self.radio


#Instancias
rect1 = Rectangulo(5, 3)
rect2 = Rectangulo(10, 8)
circ1 = Circulo(4)
circ2 = Circulo(6)

#Mostrar resultados
print(f"{rect1.nombre} 1 -> Área: {rect1.area()} | Perímetro: {rect1.perimetro()}")
print(f"{rect2.nombre} 2 -> Área: {rect2.area()} | Perímetro: {rect2.perimetro()}")
print(f"{circ1.nombre} 1 -> Área: {circ1.area():.2f} | Perímetro: {circ1.perimetro():.2f}")
print(f"{circ2.nombre} 2 -> Área: {circ2.area():.2f} | Perímetro: {circ2.perimetro():.2f}")