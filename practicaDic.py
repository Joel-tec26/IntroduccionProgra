# Creado por: Joel Porras, María José Espinoza y Alexis Torres
# Fecha de creación: 06/05/2026 10am
# Ultima modificación: 13/05/2026 3pm
# versión: 3.14

# definición de funciones

# reto 1

def autorizarConciertos(pdiccionario):
    """
    Funcionalidad:
    Cuenta la cantidad de personas menores y mayores de edad
    y muestra cuáles están autorizadas para asistir al concierto.

    Entradas:
    -pdiccionario(dict): diccionario que contiene nombres como claves
    y edades como valores

    Salidas:
    -mensaje(str): cantidad de menores y mayores de edad mostrados en pantalla
    -mensaje(str): nombres de las personas autorizadas para asistir al concierto
    """
    menores = 0
    mayores = 0
    autorizados = []
    for nombre in pdiccionario:
        edad = pdiccionario[nombre]
        if edad < 18:
            menores += 1
        else:
            mayores += 1
            autorizados.append(nombre)
    print("Menores a 18 años:", menores)
    print("Mayores o igual a 18 años:", mayores)
    print("Pueden asistir al concierto:")
    if len(autorizados) == 0:
        print("Ninguno")
    else:
        print(", ".join(autorizados))
    return
# reto 5

def obtenerProduccion (ptupla):
    """
    Funcionamiento: Sumar las cantidades a producir por cada código de celular de todas las fabricas recibidas en una tupla.
    Entradas:
    - ptupla(tupla): Contiene diccionarios, donde cada uno representa la producción de una fábrica.
    Salidas:
    - produccionTotal(diccionario): Un diccionario con los códigos de celular como llaves y el total de la producción sumada como valores
    """
    produccionTotal={}
    for fabrica in ptupla:
        for codigoCelular, cantidadProduccion in fabrica.items():
            if codigoCelular in produccionTotal:
                produccionTotal[codigoCelular] = produccionTotal[codigoCelular] + cantidadProduccion
            else:
                produccionTotal[codigoCelular] = cantidadProduccion
    return produccionTotal

# reto 7

def obtenerMatricula(pdiccNombre,pdiccMateria):
    """
    funcion: combierte 2 diccionarios (nombres y materias) en 3 listas: carnets nombres y materias
    Entradas:
    -pdiccNombre(diccionario): diccionario con key carnet de estudiante y value el nombre de ese estudiante
    -pdiccNombre(diccionario): diccionario con key numero de materia y value los carnets de los estudiantes que llevan esa materia
    Salidas:
    -carnets(lista): tiene todos los carnets de los estudiantes en orden
    -nombres(lista): tiene todos los nombres de los estudiantes en orden
    -nombres(lista): tiene todas las materias que estan llevando cada estudiante en orden
    """
    carnets=[]
    nombres=[]
    materias=[]
    for i, o in pdiccNombre.items():
        carnets.append(i)
        nombres.append(o)
        materiasEstudiantes=[]
        for j, k in pdiccMateria.items():
            if i in k: #si el carnet se encuentra en la lista de carnets de la materia j
                materiasEstudiantes.append(j)
        materias.append(tuple(materiasEstudiantes))
    return carnets, nombres, materias

# Programa principal

print("Reto 1")
print("Entrada:autorizarConciertos({'Juan': 17})")
print("salida:")
autorizarConciertos({'Juan': 17})
print("Entrada: autorizarConciertos({'Juan': 23})")
print("salida:")
autorizarConciertos({'Juan': 23})
print("Entrada: autorizarConciertos({'Juan': 17,'Mario': 21,'Oscar': 23,'Julia': 18})")
print("salida:")
autorizarConciertos({'Juan': 17,'Mario': 21,'Oscar': 23,'Julia': 18})
print()

print("Reto 5")
print("Entrada: \nobtenerProduccion(({ 'S10': 25000, 'S25': 30000, 'S8': 10000}, {'S7': 5000, 'S25': 40000}))")
print("Salida:")
print(obtenerProduccion(({"S10": 25000, "S25": 30000, "S8": 10000}, {"S7": 5000, "S25": 40000})))
print()

print("Reto7")
print("entrada: { 201780: \"William\", 201715: \"Alberto\", 201710: \"Martha\", 201760: \"Javier\" },{ 1: [ 201780, 201710 ], 2: [ 201780, 201715, 201760 ], 3: [ 201715 ], 4: [ 201780, 201715, 201710, 201760], 5: [ 201715 ] }")
salida=obtenerMatricula({ 201780: "William", 201715: "Alberto", 201710: "Martha", 201760: "Javier" },{ 1: [ 201780, 201710 ], 2: [ 201780, 201715, 201760 ], 3: [ 201715 ], 4: [ 201780, 201715, 201710, 201760], 5: [ 201715 ] })
print(f"Salida: {salida}")
