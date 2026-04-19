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
    patron = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
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

def procesarLog():
    print("\n ===============")
    print(" Opción 1")
    print("================")
    global bdVuelos
    parrafo = input("Ingrese el párrafo del log: ")
    piezas = parrafo.split()
    print("\n====Analizando piezas del log ===")
    for pieza in piezas:
        piezaLimpia = pieza.strip(",.;/-:_*")
        if validarVuelo(piezaLimpia):
            print(f"Código válido encontrado: {piezaLimpia}")
            if piezaLimpia not in bdVuelos:
                if bdVuelos == "":
                    bdVuelos = piezaLimpia
                else:
                    bdVuelos += "," + piezaLimpia
        else:
            pass 
    print("\nProcesamiento completo.")
    print(f"Vuelos registrados: {bdVuelos}")

def Ingresarpasajero():
    print("\n ===============")
    print(" Opción 2")
    print("================")
    global bdPasajeros, bdVuelos
    datoSucio = input("Ingrese datos (Nombre-Vuelo-Email): ")
    partes = datoSucio.split("-")
    if len(partes) != 3:
        print("Error: Formato incorrecto.")
        return
    nombre = normalizarNombre(partes[0])
    vuelo = partes[1].strip()
    email = partes[2].strip()
    if not validarVuelo(vuelo):
        print("Error: Vuelo inválido.")
    elif not detectarVuelo(vuelo):
        print("Error: El vuelo no existe en el Log.")
    elif not validarEmail(email):
        print("Error: Email inválido.")
    else:
        # Formato: Vuelo→Nombre→Email
        registro = f"{vuelo}→{nombre}→{email}"
        if bdPasajeros == "":
            bdPasajeros = registro
        else:
            # Separa pasajeros con ¬
            bdPasajeros += "¬" + registro
        print(f"Pasajero {nombre} registrado.")

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

def verPasajerosRegistrados():
    print("\n ===============")
    print(" Opción 4")
    print("================")
    global bdPasajeros, sumaFletes
    if bdPasajeros == "":
        print("\nNo hay pasajeros en el buffer.")
    else:
        print("\n--- Lista de pasajeros registrados ---")
        registros = bdPasajeros.split("¬")
        for r in registros:
            datos = r.split("→")
            print(f"Vuelo: {datos[0]}  Pasajero: {datos[1]}  Email: {datos[2]}")
    print("-------------")
    print(f"Total recaudado por fletes: ₡{sumaFletes:}")

