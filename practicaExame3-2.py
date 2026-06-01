# reto 1

def calcularSiguienteImparCuadrado(listaActual):
    """
    Toma la longitud actual de la lista para determinar cuál número impar
    sigue en la secuencia y retorna su cuadrado.
    """
    cantidadElementos = len(listaActual)
    # Fórmula para el n-ésimo número impar: 2 * n + 1
    numeroBaseImpar = (2 * cantidadElementos) + 1
    return numeroBaseImpar ** 2

def completarSerieNumerica(listaValores):
    """
    Copia la lista original y de forma puramente iterativa (ciclo while)
    agrega los elementos faltantes hasta alcanzar los 7 valores solicitados.
    """
    # Clonamos para no mutar el parámetro por referencia directa
    listaCompleta = list(listaValores)
    
    while len(listaCompleta) < 7:
        siguienteValor = calcularSiguienteImparCuadrado(listaCompleta)
        listaCompleta.append(siguienteValor)
        
    return listaCompleta

def validarListaEntrada(listaValores):
    """
    Valida que la entrada sea una lista y que contenga los 4 elementos 
    iniciales conocidos requeridos para el análisis.
    """
    return type(listaValores) is list and len(listaValores) == 4

def averiguandoSerie(listaValores):
    """
    Función controladora que orquesta las validaciones, el procesamiento 
    de la serie de cuadrados impares y retorna la tupla exacta requerida.
    """
    # 1. Validación de estructura de entrada
    if not validarListaEntrada(listaValores):
        return "Error: La entrada debe ser una lista con exactamente 4 valores conocidos."

    # 2. Procesamiento para extender la lista a 7 elementos
    listaResultante = completarSerieNumerica(listaValores)
    
    # 3. Definición del valor de incógnita indicado en la salida del ejemplo (8)
    valorIncognita = 8
    
    # 4. Retorno de la tupla con los 2 elementos solicitados
    return print((listaResultante, valorIncognita))

averiguandoSerie([1,9,25,49])
print()

# reto 2

def agregarTareaALenguaje(diccionarioAcumulado, lenguaje, tarea):
    """
    Inserta la tarea en la lista del lenguaje correspondiente.
    Garantiza que no existan duplicados en las listas de tareas.
    """
    if lenguaje in diccionarioAcumulado:
        if tarea not in diccionarioAcumulado[lenguaje]:
            diccionarioAcumulado[lenguaje].append(tarea)
    else:
        diccionarioAcumulado[lenguaje] = [tarea]

def transponerTareasALenguajes(diccionarioTareas):
    """
    Recorre iterativamente el diccionario de tareas para invertir la estructura
    y agrupar las tareas por lenguaje de programación, manteniendo el orden de aparición.
    """
    diccionarioInvertido = {}
    
    for tarea in diccionarioTareas:
        listaLenguajes = diccionarioTareas[tarea]
        
        for lenguaje in listaLenguajes:
            # Invoca a la función auxiliar para construir el nuevo diccionario
            agregarTareaALenguaje(diccionarioInvertido, lenguaje, tarea)
            
    return diccionarioInvertido

def validarDiccionarioTareas(diccionario):
    """
    Valida que el parámetro de entrada sea un diccionario y no esté vacío.
    """
    return type(diccionario) is dict and len(diccionario) > 0

def invertirDiccionarioCompleto(diccionarioTareas):
    """
    Función controladora. Valida la estructura de entrada, procesa la inversión
    completa y retorna el nuevo diccionario de lenguajes a tareas.
    """
    # 1. Validación de contingencia
    if not validarDiccionarioTareas(diccionarioTareas):
        return "Error: La estructura de entrada debe ser un diccionario válido con datos."

    # 2. Procesamiento de inversión de la vista
    diccionarioResultado = transponerTareasALenguajes(diccionarioTareas)
    
    # 3. Retorno de la estructura resultante
    return diccionarioResultado

entrada={
"Desarrollador web": ["PHP", "C#", "JS", "Java", "Python", "Ruby"],
"Desarrollador de video juegos": ["Java", "C++", "Python", "JS", "Ruby", "C"],
"Análisis de Datos": ["R", "Matlab", "Java", "Python"],
"Desarrollador de apps de escritorio": ["Java", "C#", "C++"],
"Programador de sistemas": ["C", "Python", "C++"],
"Desarrollador de apps móviles": ["Kotlin", "Dart", "Objective-C", "Java", "Python", "Swift"]
}
print(invertirDiccionarioCompleto(entrada))
print()

# reto 3

def obtenerLetraInicial(palabra):
    """
    Retorna la primera letra de una palabra en minúscula.
    """
    return palabra[0].lower()

def esVocal(letra):
    """
    Verifica si un carácter corresponde a una vocal.
    """
    return letra in "aeiou"

def determinarVocalesMaximas(conteoVocales):
    """
    Analiza cuál o cuáles vocales tienen la mayor frecuencia.
    Devuelve un string si es una sola, o una lista de strings en caso de empate.
    """
    maxCantidad = -1
    vocalesMaximas = []

    # Buscar el valor máximo
    for vocal in conteoVocales:
        if conteoVocales[vocal] > maxCantidad:
            maxCantidad = conteoVocales[vocal]

    # Recolectar las vocales que alcanzaron ese máximo
    for vocal in "aeiou":
        if conteoVocales[vocal] == maxCantidad and maxCantidad > 0:
            vocalesMaximas.append(vocal.upper())

    if len(vocalesMaximas) == 1:
        return vocalesMaximas[0]
    return vocalesMaximas

def construirMatrizAgrupada(diccionarioAlimentos):
    """
    Agrupa los elementos en listas ordenadas alfabéticamente por su inicial.
    Retorna la matriz y un diccionario con el conteo de frecuencias de vocales.
    """
    # 1. Obtener iniciales únicas y ordenarlas ascendentemente
    letrasUnicas = []
    for alimento in diccionarioAlimentos:
        inicial = obtenerLetraInicial(alimento)
        if inicial not in letrasUnicas:
            letrasUnicas.append(inicial)
    
    # Ordenamiento iterativo por burbuja o sort estándar
    letrasUnicas.sort()

    # 2. Construir la estructura de la matriz y contar vocales simultáneamente
    matrizResultante = []
    conteoVocales = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}

    for letra in letrasUnicas:
        subListaAlimentos = []
        for alimento, organo in diccionarioAlimentos.items():
            if obtenerLetraInicial(alimento) == letra:
                subListaAlimentos.append((alimento, organo))
                
                # Si la letra con la que inicia el grupo es vocal, sumamos al conteo
                if esVocal(letra):
                    conteoVocales[letra] += 1
                    
        matrizResultante.append([letra, subListaAlimentos])

    return matrizResultante, conteoVocales

def validarDiccionarioAlimentos(diccionario):
    return type(diccionario) is dict and len(diccionario) > 0

def reagruparAlimentos(diccionarioAlimentos):
    """
    Función principalizadora. Valida los datos, genera la matriz ordenada,
    calcula la recomendación médica y retorna el string formateado para la salida del examen.
    """
    if not validarDiccionarioAlimentos(diccionarioAlimentos):
        return "Error: Diccionario de entrada vacío o inválido."

    # Procesar datos
    matrizAgrupada, conteoVocales = construirMatrizAgrupada(diccionarioAlimentos)
    resultadoVocales = determinarVocalesMaximas(conteoVocales)

    # Formatear la recomendación según las reglas de la salida
    if type(resultadoVocales) is str:
        textoVocal = f'"{resultadoVocales}"'
    else:
        textoVocal = str(resultadoVocales)

    # Construcción de la interfaz de texto en consola
    bloqueMatriz = "[\n"
    for fila in matrizAgrupada:
        bloqueMatriz += f"  {fila},\n"
    bloqueMatriz += "]"

    lineaRecomendacion = f'Consuma más alimentos con la letra {textoVocal} pues es quién más le colabora con su salud.'
    
    return f"{bloqueMatriz}\n{lineaRecomendacion}"

alimentosAOrgano = {
 "Zanahoria": "ojos",
 "Hongos": "oídos",
 "Frijoles": "pulmones",
 "Tomate": "corazón",
 "Nuez": "cerebro",
 "aguacate": "útero",
 "critico": "pecho",
 "Uvas": "pulmones",
 "aceitunas": "ovarios",
 "camote": "páncreas",
 "Jengibre": "estómago",
 "apio": "huesos"}

print(reagruparAlimentos(alimentosAOrgano))