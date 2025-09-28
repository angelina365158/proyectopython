"""Ejercicio 9: gestión de facturas"""

facturas = {}

while True:
    opcion = input("\n1. Agregar factura\n2. Pagar factura\n3. Salir\nElija una opción: ")

    if opcion == "1":
        num_factura = input("Ingrese número de factura: ")
        costo = float(input("Ingrese el costo: "))
        facturas[num_factura] = costo
        print("Factura agregada.")

    elif opcion == "2":
        num_factura = input("Ingrese número de factura a pagar: ")
        if num_factura in facturas:
            del facturas[num_factura]
            print("La factura ya está cancelada.")
        else:
            print("El número de factura no existe.")

    elif opcion == "3":
        break

    print("Estado actual:", facturas)