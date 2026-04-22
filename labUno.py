# Creado por: Joel Jesús Porras Muñoz y Alexis Torres
# Fecha de creación: 18/04/2026 2pm
# Ultíma modificación: 22/4/2026 10am
# Versión: 3.14

# importación de funciones
from funciones import *

#Variables de tipo global
bdVuelos = ""
bdPasajeros = ""
sumaFletes = 0.0

#programa principal
while True:
    print("="*30)
    print("\t\tAerolínea Foobar\n\tSistema de Pre-check-in SkyValidator\n\nPor favor, ingrese el número de la acción que desea realizar")
    print("="*30)
    print("1.\tProcesar Bloque de Log")
    print("2.\tIngresar Pasajero")
    print("3.\tCalcular Flete")
    print("4.\tVer Pasajeros Registrados")
    print("5.\tModificar pasajeros")
    print("6.\tSalir\n")

    opcion=(input("Seleccione: "))

    if opcion=="1":
        bdVuelos=procesarLogAux(bdVuelos)
    elif opcion=="2":
        bdPasajeros= ingresarPasajerAux(bdVuelos,bdPasajeros)
    elif opcion=="3":
        sumaFletes+=calcularFleteAux(sumaFletes)
    elif opcion=="4":
        verPasajerosRegistradosAux(bdPasajeros, sumaFletes)
    elif opcion=="5":
        bdPasajeros=modificarPasajerosAux(bdPasajeros, bdVuelos)
    elif opcion=="6":
        print("cerrando...")
        break
    else:
        input("opcion no valida.\npulse ENTER para continuar:")