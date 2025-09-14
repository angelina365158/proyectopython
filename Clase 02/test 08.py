"""
Reconocimiento de tipos de datos: type()
"""

nombre = "Luis"
ciudad = "Lima"
sueldo = 5000
empresa = False
correo = "luishh@gmail.com"
empleado = [nombre, ciudad, sueldo, empresa]
empleado_4 = {'nomb': nombre, 'ciudad': ciudad, 'sueld': sueldo, 'empresa': empresa}

print("Tipo de variable para 'nombre' es {}".format(type(nombre)))
print("Tipo de variable para 'ciudad' es {}".format(type(ciudad)))
print("Tipo de variable para 'sueldo ' es {}".format(type(sueldo)))
print("Tipo de variable para 'empresa' es {}".format(type(empresa)))
print("Tipo de variable para 'correo' es {}".format(type(correo)))
print("Tipo de variable para 'empleado' es {}".format(type(empleado)))
print("Tipo de variable para 'empleado_4' es {}".format(type(empleado_4)))