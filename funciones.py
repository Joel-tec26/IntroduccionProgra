# Creado por: Joel Jesús Porras Muñoz y Alexis Torres
# Fecha de creación: 18/04/2026 2pm
# Ultíma modificación: 22/4/2026 10:15am
# Versión: 3.14

# importación de metodos
import re

# definición de funciones
# principales
def validarVuelo(ptexto):
    """
    Funcionalidad:
    Valida si un texto cumple con el formato de código de vuelo 
    (3 letras mayúsculas seguidas de 6 dígitos).
    Entradas:
    -ptexto(str): texto que representa el código de vuelo a validar
    Salidas:
    -resultado(bool): True si el formato es válido, False en caso contrario
    """
    return bool(re.match(r"^[a-zA-Z]{3}\d{6}$", ptexto))

def normalizarNombre(nombreSucio):
    """
    Funcionalidad:
    Limpia y normaliza un nombre eliminando espacios extra y aplicando 
    formato de título.
    Entradas:
    -nombreSucio(str): nombre con posibles espacios innecesarios 
    o formato incorrecto
    Salidas:
    -nombre(str): nombre limpio con la primera letra de cada palabra
    en mayúscula
    """
    return " ".join(nombreSucio.strip().split()).title()

def validarNombre(pnombre):
    """
    Funcionalidad:
    Verifica si un nombre cumple el formato
    Entradas:
    -pnombre(str): texto que e valida
    Salidas:
    -resultado(bool): True si cumple, False en caso contrario
    """
    if bool(re.match(r"^[a-zA-Zá-úä-üÁ-ÚÄ-Ü\s\.\']+$", pnombre)) and " " in pnombre.strip():
        return True
    return False
    
def detectarVuelo(bloqueTexto, bdVuelos):
    """
    Funcionalidad:
    Verifica si un código de vuelo existe dentro de la base de datos de
    vuelos.
    Entradas:
    -bloqueTexto(str): texto donde se busca el código de vuelo
    Salidas:
    -resultado(bool): True si el vuelo está presente, False en caso contrario
    """
    if bloqueTexto in bdVuelos:
        return True
    else:
        return False

def validarEmail(email):
    """
    Funcionalidad: Valida si un correo electrónico pertenece al 
    dominio floo.com y cumple con el formato básico.
    Entradas:
    -email(str): correo electrónico a validar
    Salidas:
    -resultado(bool): True si el correo es válido, False en caso contrario
    """
    patron = r"^[a-zA-Z0-9._%+-]+@foo\.com$"
    return bool(re.match(patron, email))

# funciones de calculos
def calcularFlete(pesoReal, largo, ancho, alto, opcionDestino, sumaFletes):
    """
    Funcionalidad:
    Calcula el costo de un flete considerando peso real, peso volumétrico,
    tarifas dinámicas y tipo de destino.
    Entradas:
    -pesoReal(float): peso real del paquete en kilogramos
    -largo(float): largo del paquete en centímetros
    -ancho(float): ancho del paquete en centímetros
    -alto(float): alto del paquete en centímetros
    -opcionDestino(str): tipo de destino ("1" internacional, "2" nacional)
    Salidas:
    -pesoV(float): peso volumétrico calculado
    -pesoT(float): peso tasable utilizado para el cálculo
    -totalFinal(float): monto total a pagar por el flete
    """
    #  Peso Volumétrico
    pesoV = (largo * ancho * alto) / 5000
    # Peso Tasable
    if pesoReal > pesoV:
        pesoT = pesoReal
    else:
        pesoT = pesoV
    # Tarifa Dinámica
    subtotal = 0
    if pesoT < 10:
        subtotal = 15000
    elif 10 <= pesoT <= 50:
        subtotal = pesoT * 2000
    else: 
        # Para más de 50kg: tarifa base + 12% combustible
        costoBase = pesoT * 1500
        subtotal = costoBase + (costoBase * 0.12)
    # Destino 
    totalFinal = 0
    if opcionDestino == "1": # Internacional
        totalFinal = subtotal + (subtotal * 0.15)
    elif opcionDestino == "2": # Nacional
        totalFinal = subtotal - (subtotal * 0.05)
    else:
        totalFinal = subtotal
    sumaFletes += totalFinal
    return pesoV, pesoT, totalFinal


# funciones generales 

def procesarLog(parrafo, bdVuelos):
    """
    Funcionalidad:
    Extrae códigos de vuelo válidos de un párrafo y los agrega a 
    la base de datos sin duplicados.
    Entradas:
    -parrafo(str): texto que contiene posibles códigos de vuelo
    -bdVuelos(str): base de datos actual de vuelos
    Salidas:
    -bdVuelos(str): base de datos actualizada con nuevos vuelos encontrados
    """
    piezas = parrafo.split()
    for pieza in piezas:
        piezaLimpia = pieza.upper().strip(",.;/-:_*")
        if validarVuelo(piezaLimpia):
            if piezaLimpia not in bdVuelos:
                if bdVuelos == "":
                    bdVuelos = piezaLimpia
                else:
                    bdVuelos += "," + piezaLimpia
    return bdVuelos

def procesarLogAux(bdVuelos):
    """
    Funcionalidad:Permite al usuario ingresar un párrafo, procesa los 
    códigos de vuelo y muestra los resultados en pantalla.
    Entradas:
    -parrafo(str): texto ingresado por el usuario mediante input()
    Salidas:
    -mensaje(str): impresión en pantalla con los vuelos registrados
    o mensaje de ausencia
    """
    print("\n ===============")
    print(" Opción 1")
    print("================")
    parrafo = input("Ingrese el párrafo del log: ")
    print("\n====Analizando piezas del log ===")
    bdVuelos = procesarLog(parrafo, bdVuelos)
    print("\nProcesamiento completo.")
    if bdVuelos == "":
        print("No se registró ningún vuelo")
    else:
        print(f"Vuelos registrados: {bdVuelos}")
    input("pulse ENTER para continuar: ")
    return bdVuelos

def Ingresarpasajero(datoSucio, bdPasajeros, bdVuelos):
    """
    Funcionalidad: Registra un pasajero validando formato, vuelo existente 
    y correo válido.
    Entradas:
    -datoSucio(str): datos del pasajero en formato "Nombre-Vuelo-Email"
    -bdPasajeros(str): base de datos actual de pasajeros
    -bdVuelos(str): base de datos de vuelos disponibles
    Salidas:
    -exito(bool): indica si el registro fue exitoso
    -resultado(str): nueva base de datos y nombre, o mensaje de error
    """
    partes = datoSucio.strip().split()
    if len(partes) < 3:
        return False, "Formato incorrecto. Uitilice: Nombre Apellido Vuelo Email"
    email = partes[-1].lower()
    vuelo = partes[-2].upper()
    nombreSucio = " ".join(partes[:-2])
    nombre = normalizarNombre(nombreSucio)
    if not validarNombre(nombre):
        return False, "El nombre debe ser 'Nombre Apellido' (solo letras)."
    if not validarVuelo(vuelo):
        return False, "El código de vuelo debe tener 3 letras y 6 números."
    if vuelo not in bdVuelos:
        return False, f"El vuelo {vuelo} no existe en el sistema."
    if not validarEmail(email):
        return False, f"El correo '{email}' es inválido. Debe ser Sucorreo@foo.com"
    if bdPasajeros != "":
        listaRegistros = bdPasajeros.split("¬")
        for registroExistente in listaRegistros:
            campos = registroExistente.split("→")
            if len(campos) == 3:
                vueloGuardado = campos[0].strip().upper()
                nombreGuardado = campos[1].strip()
                emailGuardado = campos[2].strip().lower()
                if vueloGuardado == vuelo:
                    return False, f"El vuelo {vuelo} ya tiene una persona registrada."
                if emailGuardado == email:
                    return False, "El email ya está en uso por otro pasajero."
    registro = f"{vuelo}→{nombre}→{email}"
    if bdPasajeros == "":
        nuevaBd = registro
    else:
        nuevaBd = bdPasajeros + "¬" + registro
    return True, (nuevaBd, nombre)

def ingresarPasajerAux(bdVuelos, bdPasajeros):
    """
    Funcionalidad:Solicita al usuario los datos de un pasajero, intenta 
    registrarlo y muestra el resultado en pantalla.
    Entradas:
    -dato(str): datos ingresados por el usuario en formato "Nombre-Vuelo-Email"
    Salidas:
    -mensaje(str): confirmación de registro o mensaje de error mostrado en pantalla
    """
    print("\n ===============")
    print(" Opción 2")
    print("================")
    if bdVuelos == "":
        print("\nNo hay vuelos registrados en el log.")
        input("pulse ENTER para continuar: ")
        return bdPasajeros
    dato = input("Ingrese datos (Nombre Apellido Vuelo Email): ")
    exito, resultado = Ingresarpasajero(dato, bdPasajeros, bdVuelos)
    if exito:
        bdPasajeros, nombreRegistrado = resultado
        print(f"Pasajero {nombreRegistrado} registrado.")
    else:
        print(resultado)
    input("pulse ENTER para continuar: ")
    return bdPasajeros

def calcularFleteAux(sumaFletes):
    """
    Funcionalidad: Solicita al usuario los datos de un paquete, calcula 
    el flete y muestra los resultados en pantalla.
    Entradas:
    -pReal(float): peso real ingresado por el usuario
    -largo(float): largo ingresado por el usuario
    -ancho(float): ancho ingresado por el usuario
    -altura(float): altura ingresada por el usuario
    -opcion(str): tipo de destino seleccionado por el usuario
    Salidas:
    -mensaje(str): impresión en pantalla con peso volumétrico, peso tasable 
    y total a pagar
    """
    print("\n ===============")
    print(" Opción 3")
    print("================")
    while True:
        try:
            pReal = float(input("Peso real de la carga (kg): "))
            if pReal <= 0:
                print("\nTodos los valores deben ser mayores a 0.")
                continue
            largo = float(input("Largo (cm): "))
            if largo <= 0:
                print("\nTodos los valores deben ser mayores a 0.")
                continue
            ancho = float(input("Ancho (cm): "))
            if ancho <= 0:
                print("\nTodos los valores deben ser mayores a 0.")
                continue
            altura = float(input("Alto (cm): "))
            if altura <= 0:
                print("\nTodos los valores deben ser mayores a 0.")
                continue
            break
        except ValueError:
            print("\nIngrese únicamente valores numéricos.")
    while True:
        print("\nSeleccione el destino:")
        print("[1] Internacional (+15% Aduana)")
        print("[2] Nacional (-5% Beneficio Local)")
        opcion = input("Digite su opción: ")
        if opcion == "1" or opcion == "2":
            break
        else:
            print(f"\n\"{opcion}\" no es una opción válida.")
            print("Por favor, digite únicamente el número 1 o el número 2.")
    volumetrico, tasable, montoPagar = calcularFlete(pReal, largo, ancho, altura, opcion, sumaFletes)
    print("\n ---------------")
    print(f"Resultados:")
    print(f"Peso Volumétrico: {volumetrico:} kg")
    print(f"Peso Tasable: {tasable:} kg")
    print(f"Total a pagar: ₡{montoPagar:}")
    print("----------------")
    print("Monto sumado al total recaudado")
    input("pulse ENTER para continuar: ")
    return montoPagar

def verPasajerosRegistrados(bdPasajeros, sumaFletes):
    """
    Funcionalidad:Retorna la base de datos de pasajeros y 
    el total acumulado de fletes.
    Entradas:
    -bdPasajeros(str): base de datos de pasajeros
    -sumaFletes(float): total acumulado de fletes
    Salidas:
    -bdPasajeros(str): lista de pasajeros
    -sumaFletes(float): total acumulado de fletes
    """
    if bdPasajeros == "":
        return "", sumaFletes
    return bdPasajeros, sumaFletes

def verPasajerosRegistradosAux(bdPasajeros, sumaFletes):
    """
    Funcionalidad: Muestra en pantalla la lista de pasajeros 
    registrados y el total recaudado.
    Entradas:
    -No tiene entradas directas 
    (usa variables globales y muestra información al usuario)
    Salidas:
    -mensaje(str): lista de pasajeros y total recaudado impresos en pantalla
    """
    print("\n ===============")
    print(" Opción 4")
    print("================")
    datosBrutos, total = verPasajerosRegistrados(bdPasajeros, sumaFletes)
    if datosBrutos == "" or datosBrutos==None:
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
    return

def modificarPasajerosAux(bdPasajeros, bdVuelos):
    """
    Funcionalidad: Permite al usuario modificar los datos de un 
    pasajero existente y muestra el resultado en pantalla.
    Entradas:
    -codigoPasajero(str): código de vuelo ingresado por el usuario
    -nuevoNombre(str): nuevo nombre ingresado por el usuario
    -nuevoCorreo(str): nuevo correo ingresado por el usuario
    Salidas:
    -mensaje(str): confirmación de modificación o mensaje de error
    mostrado en pantalla
    """
    print("\n ===============")
    print(" Opción 5")
    print("================")
    if bdPasajeros == "":
        print("\nNo hay pasajeros en el buffer.")
        input("pulse ENTER para continuar: ")
        return bdPasajeros
    codigoPasajero = input("ingrese el código de vuelo del pasajero que quiere modificar: ").strip().upper()
    if not detectarVuelo(codigoPasajero, bdVuelos) or codigoPasajero=="":
        print(f"El pasajero {codigoPasajero} no fué encontrado")
        input("pulse ENTER para continuar: ")
        return bdPasajeros
    nuevoNombre = input("ingrese el nuevo nombre: ")
    if not validarNombre(nuevoNombre):
        print ("Debe ingresar un nombre y seguir el formato de este (nombre apellido)")
        input("pulse ENTER para continuar: ")
        return bdPasajeros
    nuevoCorreo = input("ingrese el nuevo correo: ")
    if not validarEmail(nuevoCorreo):
        print("Email inválido. El email debe ser suCorreo@foo.com")
        input("pulse ENTER para continuar: ")
        return bdPasajeros
    nuevoNombre=normalizarNombre(nuevoNombre)
    nuevaLista=modificarPasajeros(nuevoNombre,nuevoCorreo,codigoPasajero, bdPasajeros)
    print("Pasajero modificado con éxito")
    input("pulse ENTER para continuar: ")
    return nuevaLista

def modificarPasajeros(nuevoNombre,nuevoCorreo,codigoPasajero, bdPasajeros):
    """
    Funcionalidad: Modifica el nombre y correo de un pasajero 
    específico en la base de datos.
    Entradas:
    -nuevoNombre(str): nuevo nombre del pasajero
    -nuevoCorreo(str): nuevo correo del pasajero
    -codigoPasajero(str): código de vuelo asociado al pasajero a modificar
    Salidas:
    -No retorna valores (actualiza la base de datos global)
    """
    nuevaLista=""
    pasajeros= bdPasajeros.split("¬")
    cantidadPasajeros=len(pasajeros)
    for i in range(cantidadPasajeros):
        pasajero=pasajeros[i].split("→")
        nombre=pasajero[1]
        correo=pasajero[2]
        codigo=pasajero[0]
        if codigo == codigoPasajero:
            nombre=nuevoNombre
            correo=nuevoCorreo
            nuevoPasajero = f"{codigo}→{nombre}→{correo}"
            if i==0:
                nuevaLista+=f"{nuevoPasajero}"
            else:
                nuevaLista+=f"¬{nuevoPasajero}"
        else:
            if i==0:
                nuevaLista+=f"{pasajeros[i]}"
            else:
                nuevaLista+=f"¬{pasajeros[i]}"
    bdPasajeros=nuevaLista
    return bdPasajeros