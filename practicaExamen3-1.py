#
#
#
# examen 3 practica 1

# reto 1 examen
def obtenerSecuenciaFactorial(n):
    """
    Generar recursivamente la lista [n, n-1, ..., 1]
    """
    if n == 1:
        return [1]
    return [n] + obtenerSecuenciaFactorial(n - 1)

def esPrimo(n, divisor=2):
    """
    Evaluar recursivamente si un número es primo o no.
    """
    if n < 2:
        return False
    if divisor * divisor > n:
        return True
    if n % divisor == 0:
        return False
    return esPrimo(n, divisor + 1)

def buscarMayorPrimoSecuencias(listaValores, indice=0, mayorPrimo=-1):
    """
    Recorrer recursivamente una lista plana buscando el primo más grande.
    """
    if indice == len(listaValores):
        return mayorPrimo
    
    numActual = listaValores[indice]
    if esPrimo(numActual) and numActual > mayorPrimo:
        mayorPrimo = numActual
        
    return buscarMayorPrimoSecuencias(listaValores, indice + 1, mayorPrimo)

def aplanarDiccionarioValores(claves, diccionario, indice=0):
    """
    Transformar los valores del diccionario en una lista plana única de forma recursiva.
    """
    if indice == len(claves):
        return []
    return diccionario[claves[indice]] + aplanarDiccionarioValores(claves, diccionario, indice + 1)

def procesarDiccionarioPares(inicio, fin, diccionarioAcumulado=None):
    """
    Construir recursivamente el diccionario con las secuencias factoriales
    de los números pares presentes en el rango.
    """
    if diccionarioAcumulado is None:
        diccionarioAcumulado = {}
    if inicio == fin:
        return diccionarioAcumulado
    if inicio % 2 == 0:
        diccionarioAcumulado[inicio] = obtenerSecuenciaFactorial(inicio)
    return procesarDiccionarioPares(inicio + 1, fin, diccionarioAcumulado)

# validaciones
def validarEsTupla(rango):
    """
    Verificar que la estructura de entrada corresponda a una tupla.
    """
    return type(rango) is tuple

def validarOrdenRango(rango):
    """
    Verificar que el límite superior sea mayor que el inferior.
    """
    return rango[1] > rango[0]

# controladora
def generarSecuencia(rango):
    """
    Función principalizadora del requerimiento. Valida la estructura,
    procesa las series del rango e imprime los pasos solicitados en el diseño.
    """
    # 1. Validaciones de entrada
    if not validarEsTupla(rango):
        return "Debe indicar una tupla para poder ser analizado."

    if not validarOrdenRango(rango):
        return "El segundo valor de la tupla debe ser mayor al primero."

    # 2. Paso 1: Procesamiento y construcción de secuencias
    inicio, fin = rango
    diccionarioFactorial = procesarDiccionarioPares(inicio, fin)
    
    print("Paso 1.")
    print("Generar el diccionario de las secuencias factoriales en una lista para")
    print("los números pares del rango. Muestre los valores factoriales")
    print("estrictamente en orden decreciente.")
    print(diccionarioFactorial)
    
    # 3. Paso 2: Búsqueda del elemento primo mayor
    clavesDiccionario = list(diccionarioFactorial.keys())
    valoresPlanos = aplanarDiccionarioValores(clavesDiccionario, diccionarioFactorial)
    mayorPrimo = buscarMayorPrimoSecuencias(valoresPlanos)
    
    print("Paso 2.")
    print("Determinar el primo más grande de los valores generados en el diccionario.")
    print(f"El primo más grande generado en la secuencia Factorial del diccionario es: {mayorPrimo}")
    
    return diccionarioFactorial

generarSecuencia([5,2])
generarSecuencia((5,2)) 
generarSecuencia((2,7))


# reto 2

def determinarCategoriaEstudiante(nota1, nota2):
    """
    Evalúa las notas de los dos parciales para asignar la categoría correspondiente.
    """
    if nota1 >= 90 and nota2 >= 90:
        return "Excelente"
    
    if nota1 >= 70 and nota2 >= 70:
        return "Muy bien"
    
    if 60 <= nota1 <= 70 and 60 <= nota2 <= 70:
        return "En riesgo"
    
    if (nota1 >= 60 or nota2 >= 60):
        return "Regular"
    
    return "Deplorable"

def clasificarEstudiantes(listaEstudiantes):
    """
    Recorre la lista construyendo el diccionario respetando estrictamente 
    el orden de aparición de las categorías (orden de inserción).
    """
    diccionarioEstados = {}
    
    for i in range(len(listaEstudiantes)):
        nota1, nota2 = listaEstudiantes[i]
        categoria = determinarCategoriaEstudiante(nota1, nota2)
        
        if categoria in diccionarioEstados:
            diccionarioEstados[categoria].append(i + 1)
        else:
            diccionarioEstados[categoria] = [i + 1]
            
    return diccionarioEstados

# validar
def validarListaNoVacia(listaEstudiantes):
    """
    Verifica que la lista de estudiantes contenga elementos a procesar.
    """
    return len(listaEstudiantes) > 0

def validarEstructuraTuplas(listaEstudiantes):
    """
    Verifica de forma iterativa que todos los elementos sean tuplas de 2 notas.
    """
    for elemento in listaEstudiantes:
        if type(elemento) is not tuple or len(elemento) != 2:
            return False
    return True
# controladora
def definirEstados(listaEstudiantes):
    """
    Función controladora. Valida, procesa y calcula las frecuencias de GTH.
    Retorna un string formateado para que el print(definirEstados(...)) externo
    dibuje el diccionario primero y la observación inmediatamente abajo.
    """
    # 1. Validaciones preventivas
    if not validarListaNoVacia(listaEstudiantes):
        return "La lista de estudiantes se encuentra vacía."
        
    if not validarEstructuraTuplas(listaEstudiantes):
        return "Estructura inválida. Todos los registros deben ser tuplas de 2 notas."

    # 2. Procesamiento
    diccionarioEstados = clasificarEstudiantes(listaEstudiantes)
    
    # 3. Análisis de frecuencias para GTH
    maxTamano = 0
    todosIguales = True
    categoriasMaximas = []
    
    categoriasActivas = list(diccionarioEstados.keys())
    primerTamano = len(diccionarioEstados[categoriasActivas[0]])
    
    for cat in categoriasActivas:
        tamanoActual = len(diccionarioEstados[cat])
        
        if tamanoActual != primerTamano:
            todosIguales = False
            
        if tamanoActual > maxTamano:
            maxTamano = tamanoActual
            categoriasMaximas = [cat]
        elif tamanoActual == maxTamano:
            categoriasMaximas.append(cat)

    # 4. Construcción de la observación de GTH basada en las reglas
    observacionGTH = ""
    
    # Si todos los grupos activos tienen el mismo tamaño y están las 5 categorías,
    # o si todos los grupos activos tienen el mismo tamaño (como en el ejemplo 3 de la imagen)
    if todosIguales:
        observacionGTH = "Los resultados estuvieron muy homogéneos."
    elif len(categoriasMaximas) == 1:
        observacionGTH = f"Considere que predominó: *{categoriasMaximas[0]}*"
    else:
        observacionGTH = f"Considere que predominaron con empate: *{', '.join(categoriasMaximas)}*"

    # 5. RETORNO DE SALIDA FORMATEADA:
    # Convertimos el diccionario a string y le concatenamos la observación con un salto de línea.
    # De esta forma, el print() externo pintará la estructura exactamente en el orden correcto.
    return f"{diccionarioEstados}\n{observacionGTH}"


print(definirEstados([(90,99),(63,72),(85,90),(87,71)]))
print(definirEstados([(23,17),(63,72),(85,90),(87,71),(100,100)]))
print(definirEstados([(63,67),(22,45),(67,71),(87,71)]))

# reto 3

def limpiarNombreLenguaje(lenguaje):
    """
    Normaliza sutilmente las cadenas para evitar duplicaciones por errores 
    de mayúsculas en el diccionario de origen (ej: 'java' -> 'Java').
    """
    if lenguaje.lower() == "java":
        return "Java"
    return lenguaje

def invertirVistaDiccionario(diccionarioEmpresas):
    """
    Construye de forma iterativa el diccionario invertido donde las llaves
    son los lenguajes y los valores son las listas de compañías que los usan.
    """
    diccionarioLenguajes = {}
    
    for compania in diccionarioEmpresas:
        listaLenguajes = diccionarioEmpresas[compania]
        
        for lang in listaLenguajes:
            langNormalizado = limpiarNombreLenguaje(lang)
            
            if langNormalizado in diccionarioLenguajes:
                # Evita repetir compañías dentro de la lista del mismo lenguaje
                if compania not in diccionarioLenguajes[langNormalizado]:
                    diccionarioLenguajes[langNormalizado].append(compania)
            else:
                diccionarioLenguajes[langNormalizado] = [compania]
                
    return diccionarioLenguajes

def calcularMetricasUso(diccionarioLenguajes):
    """
    Genera la lista de tuplas (Lenguaje, Cantidad) y determina de forma iterativa
    cuál es el lenguaje más utilizado por las compañías.
    """
    listaTuplasRespuesta = []
    maxUso = -1
    lenguajeMasUsado = ""
    
    for lenguaje in diccionarioLenguajes:
        cantidadCompanias = len(diccionarioLenguajes[lenguaje])
        listaTuplasRespuesta.append((lenguaje, cantidadCompanias))
        
        # Guardar el de mayor uso (si hay empate, conserva el primero o aplica criterio simple)
        if cantidadCompanias > maxUso:
            maxUso = cantidadCompanias
            lenguajeMasUsado = lenguaje
            
    return listaTuplasRespuesta, lenguajeMasUsado


# validar
def validarDiccionarioEntrada(diccionario):
    """
    Valida que la entrada sea un diccionario y que no se encuentre vacío.
    """
    return type(diccionario) is dict and len(diccionario) > 0

# controlar
def transformarDiccionario(entrada):
    """
    Función controladora principal. Valida la entrada, ejecuta la Parte 1
    y la Parte 2, y retorna un string unificado para su correcta visualización.
    """
    # 1. Validación de contingencia
    if not validarDiccionarioEntrada(entrada):
        return "Estructura de entrada inválida o vacía."

    # 2. Parte 1: Transformación de la vista
    salidaDiccionarioInvertido = invertirVistaDiccionario(entrada)
    
    # 3. Parte 2: Lenguaje que más se usa en las compañías
    listaRespuestaTuplas, lenguajeMasUsado = calcularMetricasUso(salidaDiccionarioInvertido)
    
    # 4. Construcción y formateo del String de salida general
    bloqueSalida = "salida=" + str(salidaDiccionarioInvertido) + "\n\n"
    bloqueParte2 = "respuesta=" + str(listaRespuestaTuplas) + "\n\n"
    bloqueConclusion = f"Por ende: {lenguajeMasUsado} es el lenguaje más usado en las compañías."
    
    # Retorna el bloque completo concatenado
    return f"{bloqueSalida}{bloqueParte2}{bloqueConclusion}"

entrada={
"Youtube":["javascript","C","C++","Go","Java","Python"],
"Google":["javascript","C","C++","Go","Java","Python"],
"Yahoo":["javascript","PHP"],
"Amazon":["javascript","java","C++","Perl"],
"Microsoft":["javascript","ASP.NET"],
"Wikipedia":["javascript","PHP","Hack"],
"eBay.com":["javascript","Java","Scala"],
"Pinterest":["javascript","Django(Python)","Erlang"],
"MSN":["javascript","ASP.NET"],
"Twitter":["javascript","C++","Java","Scala","Ruby on Rails"],
"Facebook":["javascript","Hack","PHP","Python","C++","Java","Erlang","D","Xhp","Hashkell"],
}
print()
print(transformarDiccionario(entrada))