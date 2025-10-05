"""Ejercicio 8: agenda de contactos"""

agenda = {}

while True:
    opcion = input("\n1. Agregar contacto\n2. Buscar contacto\n3. Salir\nElija una opción: ")

    if opcion == "1":
        nombre = input("Ingrese nombre: ")
        telefono = input("Ingrese teléfono: ")
        agenda[nombre] = telefono
        print("Contacto agregado con éxito")

    elif opcion == "2":
        buscar = input("Ingrese nombre a buscar: ")
        if buscar in agenda:
            print(f"{buscar}: {agenda[buscar]}")
        else:
            print("No se encuentra registrado en la agenda.")

    elif opcion == "3":
        break
    else:
        print("Opción inválida.")