#Para main
from validador import validar_usuario

#Pedir al usuario ingresar un nombre
usuario = input("Ingrese un nombre de usuario: ")

#Validar el nombre usando la función del módulo
resultado = validar_usuario(usuario)

#Por ultimo mostrar el resultado
if resultado == True:
    print("Nombre de usuario válido")
else:
    print("Error:", resultado)