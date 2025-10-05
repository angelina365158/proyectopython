"""Crear una clase llamada Circulo que contenga radio en su constructor y
que contenga un metodo area que devuelva el area de un círculo"""

import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def pedir_radio(self):
        self.radio = float(input("Ingrese el radio del círculo: "))

    def area(self):
        return math.pi * self.radio ** 2

    def perimetro(self):
        return 2 * math.pi * self.radio


# Instanciación de 2 círculos
circulo1 = Circulo(5)
circulo2 = Circulo(10)

print(f"Área del círculo 1: {circulo1.area():.2f}")
print(f"Perímetro del círculo 1: {circulo1.perimetro():.2f}")

print(f"Área del círculo 2: {circulo2.area():.2f}")
print(f"Perímetro del círculo 2: {circulo2.perimetro():.2f}")