# Creado por: Joel Jesús Porras Muñoz y Alexis Torres
# Fecha de creación: 18/04/2026 2pm
# Ultíma modificación: 19/4/2026 6pm
# Versión: 3.14

# importación de funciones
from funciones import *

#programa principal
while True:
    print("\t\tAerolínea Foobar\n\tSistema de Pre-check-in SkyValidator\n\nPor favor, ingrese el número de la acción que desea realizar")
    print("1.\tProcesar Bloque de Log")
    print("2.\tIngresar Pasajero")
    print("3.\tCalcular Flete")
    print("4.\tVer Pasajeros Registrados")
    print("5.\tModificar pasajeros")
    print("6.\tSalir\n")

    opcion=(input("Seleccione: "))

    if opcion=="1":
        procesarLogaux()
    elif opcion=="2":
        ingresarPasajeraux()
    elif opcion=="3":
        calcularFleteaux()
    elif opcion=="4":
        verPasajerosRegistradosaux()
    elif opcion=="5":
        modificarPasajerosaux()
    elif opcion=="6":
        print("cerrando...")
        break
    else:
        input("opcion no valida.\npulse ENTER para continuar:")