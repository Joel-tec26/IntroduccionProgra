# Creado por:
# Fecha de creación:
# Ultíma modificación:
# Versión:

# importación de metodos
import re

#Variables de tipo global
bdVuelos = ""
bdPasajeros = ""
sumaFletes = 0.0

# definición de funciones

#validaciones
def validarVuelo(ptexto):
    return bool(re.match(r"^[A-Z]{3}\d{6}$", ptexto))

def normalizarNombre(nombreSucio):
    return " ".join(nombreSucio.strip().split()).title()
    
def detectarVuelo(bloqueTexto):
    global bdVuelos
    if bdVuelos in bloqueTexto:
        return True
    else:
        return False

def validarEmail(email):
    patron = r"^[a-zA-Z0-9._%+-]+@+floo+\.+com$"
    return bool(re.match(patron, email))

# funciones de calculos
def calcularFlete(pesoReal, largo, ancho, alto, opcionDestino):
    global sumaFletes
    #  Peso Volumétrico
    pV = (largo * ancho * alto) / 5000
    # Peso Tasable
    if pesoReal > pV:
        pT = pesoReal
    else:
        pT = pV
    # Tarifa Dinámica
    subtotal = 0
    if pT < 10:
        subtotal = 15000
    elif 10 <= pT <= 50:
        subtotal = pT * 2000
    else: 
        # Para más de 50kg: tarifa base + 12% combustible
        costoBase = pT * 1500
        subtotal = costoBase + (costoBase * 0.12)
    # Destino 
    totalFinal = 0
    if opcionDestino == "1": # Internacional
        totalFinal = subtotal + (subtotal * 0.15)
    elif opcionDestino == "2": # Nacional
        totalFinal = subtotal - (subtotal * 0.05)
    else:
        totalFinal = subtotal
    #  variable global
    sumaFletes += totalFinal
    return pV, pT, totalFinal


# funciones generales 

def procesarLog(parrafo, bdVuelos):
    """
    """
    piezas = parrafo.split()
    for pieza in piezas:
        piezaLimpia = pieza.strip(",.;/-:_*")
        
        # Se asume que validarVuelo existe en otra parte del código
        if validarVuelo(piezaLimpia):
            if piezaLimpia not in bdVuelos:
                if bdVuelos == "":
                    bdVuelos = piezaLimpia
                else:
                    bdVuelos += "," + piezaLimpia
    return bdVuelos

def procesarLogaux():
    """
    """
    global bdVuelos
    print("\n ===============")
    print(" Opción 1")
    print("================")
    parrafo = input("Ingrese el párrafo del log: ")
    print("\n====Analizando piezas del log ===")
    bdVuelos = procesarLog(parrafo, bdVuelos)
    print("\nProcesamiento completo.")
    print(f"Vuelos registrados: {bdVuelos}")
    input("pulse ENTER para continuar: ")

def Ingresarpasajero(datoSucio, bdPasajeros, bdVuelos):
    """
    """
    partes = datoSucio.split("-")
    if len(partes) != 3:
        return False, "Error: Formato incorrecto."
    nombre = normalizarNombre(partes[0])
    vuelo = partes[1].strip()
    email = partes[2].strip()
    if not validarVuelo(vuelo):
        return False, "Error: Vuelo inválido."
    if vuelo not in bdVuelos:
        return False, "Error: El vuelo no existe en el Log."
    if not validarEmail(email):
        return False, "Error: Email inválido."
    registro = f"{vuelo}→{nombre}→{email}"
    if bdPasajeros == "":
        nuevaBd = registro
    else:
        nuevaBd = bdPasajeros + "¬" + registro
        
    return True, (nuevaBd, nombre)

def Ingresarpasajeraux():
    """
    """
    global bdPasajeros, bdVuelos
    print("\n ===============")
    print(" Opción 2")
    print("================")
    dato = input("Ingrese datos (Nombre-Vuelo-Email): ")
    exito, resultado = Ingresarpasajero(dato, bdPasajeros, bdVuelos)
    if exito:
        bdPasajeros, nombreRegistrado = resultado
        print(f"Pasajero {nombreRegistrado} registrado.")
    else:
        print(resultado)
    input("pulse ENTER para continuar: ")

def calcularFleteaux():
    print("\n ===============")
    print(" Opción 3")
    print("================")
    # Pedir datos al usuario
    pReal = float(input("Peso real de la carga (kg): "))
    largo = float(input("Largo (cm): "))
    ancho = float(input("Ancho (cm): "))
    altura = float(input("Alto (cm): "))
    while True:
        print("\nSeleccione el destino:")
        print("[1] Internacional (+15% Aduana)")
        print("[2] Nacional (-5% Beneficio Local)")
        opcion = input("Digite su opción: ")
        if opcion == "1" or opcion == "2":
            break
        else:
            print(f"\n¡Error! {opcion} no es una opción válida.")
            print("Por favor, digite únicamente el número 1 o el número 2.")
    volumetrico, tasable, montoPagar = calcularFlete(pReal, largo, ancho, altura, opcion)
#resultados al usuario
    print("\n ---------------")
    print(f"Resultados:")
    print(f"Peso Volumétrico: {volumetrico:} kg")
    print(f"Peso Tasable: {tasable:} kg")
    print(f"Total a pagar: ₡{montoPagar:}")
    print("----------------")
    print("Monto sumado al total recaudado")
    input("pulse ENTER para continuar: ")

def verPasajerosRegistrados(bdPasajeros, sumaFletes):
    """
    """
    if bdPasajeros == "":
        return "", sumaFletes
    return bdPasajeros, sumaFletes

def verPasajerosRegistradosaux():
    """
    """
    global bdPasajeros, sumaFletes
    print("\n ===============")
    print(" Opción 4")
    print("================")
    datosBrutos, total = verPasajerosRegistrados(bdPasajeros, sumaFletes)
    if datosBrutos == "":
        print("\nNo hay pasajeros en el buffer.")
    else:
        print("\n--- Lista de pasajeros registrados ---")
        for registro in datosBrutos.split("¬"):
            detalles = registro.split("→")
            vuelo = detalles[0]
            nombre = detalles[1]
            email = detalles[2]
            print(f"Vuelo: {vuelo}  Pasajero: {nombre}  Email: {email}")
    print("-------------")
    print(f"Total recaudado por fletes: ₡{total}")
    input("pulse ENTER para continuar: ")