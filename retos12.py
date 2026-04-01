# creador por: Joel Jesús Porras Muñoz, Alexis Torres, María José Espinoza Ortega y Cristopher Jara Salazar
# Fecha de creación: 13/3/2026 8:30am
# Ultima modificación: 17/03/2026 21:12pm
# versión: 3.14.3

# Definición de funciones

# reto 1

def obtenerFactorial(pnum):
    """
    Funcionalidad:
    calcular el factorial
    entradas:
    -pnum(int): número al cual hay que calularle el factorial
    salidas:
    -presultado(int): número de factorial
    """
    presultado = 1
    contador = 1
    while contador <= pnum:
        presultado = presultado * contador
        contador = contador + 1
    return presultado

def validarEntrada(pnum):
    """
    funcionalidad:
    Validar que el número de entrada sea un entero
    entradas:
    -pnum(int): número al cual hay que valorar que este correcto
    salidas:
    - Número incorrecto (str): corrige al usuario
    - Número factorial calculado
    """
    if not isinstance(pnum, int):
        return "Debe indicar un número entero"
    if pnum <= 0:
        return "El número debe ser mayor a cero"
    return obtenerFactorial(pnum)

#Reto 2
def validarEnteroPositivo(valor):
    """
    Funcionalidad:
        Determina si el valor ingresado es un número entero positivo. 
        Valida que no contenga decimales, que sea un carácter numérico 
        y que su valor sea estrictamente mayor a cero.
    Entradas:
        - valor (any): Dato recibido (usualmente string) que se desea validar.
    Salidas:
        - int: El número convertido si cumple con todas las condiciones.
        - None: Si el valor es menor/igual a cero, contiene decimales o no es numérico.
    """
    try:
        numero = int(valor)
        if numero > 0:
            return numero
        else:
            print("Debe ser mayor a 0")
            return 
    except:
        if "." in valor:
            print("Debe ingresar unicamente un entero")
        else:
            print("Debe ingresar unicamente un numero")
        return 

def obtenerSumatoria(n):
    """
    Funcionalidad:
    Calcula la suma de los cuadrados de los primeros 'n' números naturales
    (1² + 2² + 3² + ... + n²) utilizando un ciclo iterativo.
    Entradas:
    - n (int): El límite superior de la serie de números a elevar al cuadrado.
    Salidas:
    - int: El resultado total de la sumatoria acumulada.
    """
    suma = 0
    i = 1
    while i <= n:
        suma = suma + (i * i)
        i = i + 1
    return suma

#reto 3

def encontrarAlmenosUnCero(pnum):
    """
    Funcionalidad:
    determina si en un número hay al menos 1 cero
    entradas:
    -pnum(int): número al que le buscan algun cero
    salidas:
    -texto indicando si posee 0 o no
    """
    tieneCero=False
    while pnum!=0:
        if pnum%10==0:
            tieneCero=True
        pnum//=10
    if tieneCero:
        return "Posee al menos un cero"
    else:
        return "No posee ningún cero"
    
def validarEncontrarAlmenosUnCero(pnum):
    """
    funcionalidad: verifica que los datos ingresados sean validos
    entradas:
    -pnum(int):numero ingresado
    salidas:N/A
    """
    while True:
        try:
            return encontrarAlmenosUnCero(pnum)
        except: ValueError


# reto 4
def determinarMayor(pnum):
    """
    Funcionalidad:
    buscar el dígito mayor empleando divisiones sucesivas
    entradas:
    -pnum(int): número al cual le vamos a encontrar el mayor
    salidas:
    -mayor(int): número mayor de la cantidad digitada
    """
    mayor = 0
    if pnum == 0:
        return 0
    while pnum > 0:
        digito = pnum % 10
        if digito > mayor:
            mayor = digito
        pnum = pnum // 10
    return mayor


def validarEntrada4(pnum):
    """
    Funcionalidad:
    Validar que el número de entrada sea un entero
    entradas:
    -pnum(int): número al cual hay que valorar que este correcto
    salidas:
    - Número incorrecto (str): corrige al usuario
    - Número mayor identificado
    """
    # En caso de que este vacío
    if pnum == "" or pnum == " ":
        return "Debe ingresar un valor numérico"
    # Tipo incorrecto
    if not isinstance(pnum, int):
        return "El valor debe ser únicamente entero"
    return determinarMayor(pnum)

#Reto 5
def esPar(pnum):
    """
    Funcionalidad:
    Determina si un número entero es par verificando si el resto de su división entre dos es igual a cero.
    Entradas:
    - pnum (int): El número que se desea evaluar.
    Salidas:
    - bool: True si el número es par, False si es impar.
    """
    return pnum % 2 == 0

def multiplicarImpares(num):
    """
    Funcionalidad:
    Extrae cada dígito de un número y calcula el producto de todos 
    aquellos que sean impares. Si el número original no contiene 
    dígitos impares, el resultado final es cero.
    Entradas:
    - num (int): Número entero positivo del cual se procesarán los dígitos.
    Salidas:
    - int: El producto de los dígitos impares encontrados, o 0 si no hubo ninguno.
    """
    resultado = 1
    hayImpar = False
    while num > 0:
        digito = num % 10
        if esPar(digito) == False:
            resultado = resultado * digito
            hayImpar = True
        num = num // 10
    if hayImpar == False:
        return 0
    return resultado

#reto 6

def contarRepeticiones(pnum, pdigito):
    """
    Funcionalidad:
    determina la cantidad de veces que aparece un número en una cifra numérica positiva mayor a cero
    entradas:
    -pnum(int): número al que buscan repeticiones con el digito
    -pdigito(int): digito que se repite
    salidas:
    -contador(int): acumula la cantidad de veces que se repite el digito
    """
    contador=0
    if pnum > 0:
        while pnum!=0:
            if pnum%10==pdigito:
                contador+=1
            pnum//=10
        return contador
    else:
        print("el numero no es mayor a 0, intentelo otra vez")

def validarContarRepeticiones(pnum, pdigito):
    """
    funcionalidad: verifica que los datos ingresados sean validos
    entradas:
    -pnum(int):numero ingresado
    -pdigito:digito ingresado
    salidas:N/A
    """
    while True:
        try:
            return contarRepeticiones(pnum, pdigito)
        except: ValueError
    

# Reto 7
def elevarNumero(pbase, pexponente):
    """
    Funcionalidad:
    calcula la potencia en bucle
    entradas:
    -pbase(int): base
    -pexponente(int): exponente
    salidas:
    -resultado(int): resultado de la potencia
    """
    resultado = 1
    contador = 0
    while contador < pexponente:
        resultado = resultado * pbase
        contador = contador + 1
    return resultado

def validarEntrada7(pbase, pexponente):
    """
    Funcionalidad:
    Validar que el número de entrada sea un entero, y cicla hasta que se cumpla
    entradas:
    -pbase(int): número de la base del número
    -pexponente(int): número del exponente del número
    salidas:
    -resultado(int): calculo final de la base elevada al exponente
    """
    #  En caso de que este vacío
    if pbase == "" or pbase == " " or pexponente == "" or pexponente == " ":
        return "Debe ingresar un valor numérico"
    # Tipo incorrecto
    if not isinstance(pbase, int) or not isinstance(pexponente, int):
        return "Debe indicar un número entero"
    # Restricción por el cero
    if pbase < 0 or pexponente < 0:
        return "El número debe ser mayor o igual a cero"
    return elevarNumero(pbase, pexponente)

# Reto 8
def validarEnteroNoNegativo(valor):
    """
    Funcionalidad:
    Valida que la entrada sea un número entero y que no sea negativo (mayor 
    o igual a cero). Si la entrada es inválida, muestra un mensaje de 
    error específico según el tipo de fallo.
    Entradas:
    - valor (any): El dato que se desea validar.
    Salidas:
    - int: El número convertido si es válido.
    - None: Si el valor es negativo, contiene decimales o no es numérico.
    """
    try:
        numero = int(valor)
        if numero >= 0:
            return numero
        else:
            print("El número debe ser mayor a 1")
            return 
    except:
        if "." in valor:
            print("El número debe ser entero")
        else:
            print("El número debe ser entero")
        return 

def esNumeroPrimo(n):
    """
    Funcionalidad:
    Determina si un número dado es primo. Un número es primo si es mayor 
    que 1 y no tiene divisores positivos distintos de 1 y de sí mismo.
    Entradas:
    -n (int): El número entero que se va a evaluar.
    Salidas:
    -bool: True si el número es primo, False en caso contrario.
    """
    if n <= 1:
        return False
    i = 2
    while i < n:
        if n % i == 0:
            return False
        i = i + 1
    return True

# Reto 9
def sumarDigitosMultiplos(pnum, pdigito):
    """
    Funcionalidad:
    suma todos los numeros que sean multiplos del digito ingresado
    entradas:
    -pnum(int): numero ingresado por el usuario
    pdigito(int): digito ingresado por el usuario para sumar los multiplos a este
    salidas:
    -suma(int): la suma total de esos numeros
    """
    suma=0
    while pnum!=0:
        ultimoDigito=pnum%10
        if (ultimoDigito%10)%pdigito==0:
            suma+=ultimoDigito
        pnum//=10
    return suma

def validarSumarDigitosMultiplos(pnum, pdigito):
    """
    funcionalidad: verifica que los datos ingresados sean validos
    entradas:
    -pnum(int):numero ingresado
    -pdigito:digito ingresado
    salidas:N/A
    """
    while True:
        try:
            return sumarDigitosMultiplos(pnum, pdigito)
        except: ValueError

# Reto 10

def esBinario(pcifra):
    """
    Funcionalidad:
    Validar que el número sea binario
    entradas:
    -pcifra(int): es el número que se va a evaluar haber si cumple con la condición de ser binario o no
    salidas:
    -El valor es binario(str): afirma que es bianrio
    -El valor no es binario(str): niega que el valor sea binario 
    """
    pnum = abs(pcifra)
    if pnum == 0:
        return "El valor es binario"
    while pnum > 0:
        ultimoDig = pnum % 10
        if ultimoDig != 0 and ultimoDig != 1:
            return "El valor no es binario"
        pnum = pnum // 10
    return "El valor es binario"

def validarEntrada10(pcifra):
    """
    Funcionalidad:
    Validar que el número de entrada sea un entero
    entradas:
    pcifra(int): es el número que se va a evaluar, y analiza si es entero, string o float
    salidas:
    -El valor es binario(str): afirma que es bianrio
    -El valor no es binario(str): niega que el valor sea binario 
    -Debe ingresar un valor númerico(str): Expone el error del usuario al ingresar un string
    -El valor debe ser unicamente entero(str): Expone el error del usuario al ingresar un float
    """
    #  En caso de que este vacío
    if pcifra == "" or pcifra == " ":
        return "Debe ingresar un valor numérico"
    # Si es string 
    if isinstance(pcifra, str):
        return "El valor debe ser únicamente entero"
    # Si no es entero 
    if not isinstance(pcifra, int):
        return "El valor debe ser únicamente entero"
    return esBinario(pcifra)

# Reto 11
def validarBinario(valor):
    """
    Funcionalidad:
    Verifica que la entrada sea un número entero y que esté compuesto 
    únicamente por los dígitos 0 y 1. Si el número contiene dígitos 
    del 2 al 9, informa que no es un sistema binario.
    Entradas:
    - valor (any): El dato que se desea validar.
    Salidas:
    - int: El número convertido si es una representación binaria válida.
    - None: Si el valor no es numérico o contiene dígitos distintos de 0 o 1.
    """
    try:
        numero = int(valor)
        while numero > 0:
            digito = numero % 10
            if digito != 0 and digito != 1:
                print("El número a convertir debe ser binario")
                return 
            numero = numero // 10
        return int(valor)
    except:
        print("Debe ingresar unicamente un numero")
        return 

def binarioADecimal(num):
    """
    Funcionalidad:
    Convierte un número en base 2 (binario) a su equivalente en base 10 
    (decimal). Procesa el número dígito por dígito de derecha a izquierda, 
    multiplicando cada uno por la potencia de 2 correspondiente.
    Entradas:
    - num (int): El número binario que se desea convertir.
    Salidas:
    - int: El valor resultante en el sistema decimal.
    """
    decimal = 0
    potencia = 0
    while num > 0:
        digito = num % 10
        decimal = decimal + (digito * (2 ** potencia))
        potencia = potencia + 1
        num = num // 10
    return decimal

# Reto 12
def mostrarAnnosBisiestos(panno1,panno2):
    """
    Funcionalidad:
    muestra los años bisiestos entre 2 años
    entradas:
    -panno1(int): primer año ingresado y mas pequeño
    -panno2(int): segundo año ingresado y mas grande
    -annosB(int): cantidad de años bisiestos (para ver si no hay)
    salidas:
    -salida(string): todos los años bisiestos encontrados convertidos en un unico string
    """
    salida=""
    annosB=0
    while panno2>=panno1:
        if panno1%4==0:
            salida+=str(panno1)+" "
            annosB+=1
        panno1+=1
    if annosB==0:
        return "No hay años bisiestos."
    return salida

def validarMostrarAnnosBisiestos(panno1, panno2):
    """
    Funcionalidad: verifica que los datos ingresados sean validos
    entradas:
    -panno1(int):primer año ingresado
    -panno2:segundo año ingresado
    salidas:N/A
    """
    while True:
        try:
            return mostrarAnnosBisiestos(panno1, panno2)
        except: ValueError

# Programa principal reto 1
print("Reto 1: Escriba una función iterativa llamada obtenerfactorial que reciba un número y devuelva su factorial.")
print("Entrada:", 5)
print("Salida:", validarEntrada(5))
print("Entrada:", 7)
print("Salida:", validarEntrada(7))
print("Entrada:", 3)
print("Salida:", validarEntrada(3))
print()

# Programa principal reto 2
print("Reto 2: Escriba una función iterativa llamada obtenerSumatoria que reciba un número \ny calcule el valor de la sumatoria.")
print("Entrada:", 2)
print("Salida:", obtenerSumatoria(2))
print("Entrada:", 6)
print("Salida:", obtenerSumatoria(6))
print("Entrada:", 5)
print("Salida:", obtenerSumatoria(5))
print("Entrada:", 7)
print("Salida:", obtenerSumatoria(7))
print("Entrada:", 0)
print("Salida:", obtenerSumatoria(0))
print("Entrada:", "a")
n = validarEnteroPositivo("a")
if n != None:
    print("Salida:", obtenerSumatoria(n))
print("Entrada:", 9.0)
n = validarEnteroPositivo(str(9.0))
if n != None:
    print("Salida:", obtenerSumatoria(n))
print()

#programa principal reto 3
print("Reto 3 encontrar el menos cero en un número")
print("entradas:",876543)
print("salida: ",validarEncontrarAlmenosUnCero(876543))
print("entradas:",1203423)
print("salida: ",validarEncontrarAlmenosUnCero(1203423))
print("entradas:",3405403465)
print("salida: ",validarEncontrarAlmenosUnCero(3405403465))
print()

# Programa principal reto 4
print("Reto 4: Implementar una función iterativa llamada determinarMayor que determina el número más grande de la cifra numérica.")
print("Entrada:", "")
print("Salida:", validarEntrada4(""))
print("Entrada:", "23e")
print("Salida:", validarEntrada4("23e"))
print("Entrada:", 2)
print("Salida:", validarEntrada4(2))
print("Entrada:", 349567)
print("Salida:", validarEntrada4(349567))
print("Entrada:", 12454321)
print("Salida:", validarEntrada4(12454321))
print("Entrada:", 123745)
print("Salida:", validarEntrada4(123745))
print()

# Programa principal reto 5
print("Reto 5: Multiplicar impares")
print("Entrada:", 12345)
print("Salida:", multiplicarImpares(12345))
print("Entrada:", 34567)
print("Salida:", multiplicarImpares(34567))
print("Entrada:", 246)
print("Salida:", multiplicarImpares(246))
print()

# Programa principal reto 6
print("Reto 6 contar cantidad de apariciones")
print("entradas:",3495967,9)
print("salida: ",validarContarRepeticiones(3495967,9))
print("entradas:",3495967,4)
print("salida:",validarContarRepeticiones(12312345,4))
print()

# Programa Principal reto 7
print("Reto 7: Codificar una función iterativa en Python, llamada elevarNumero, que permita elevar un número entero a una potencia indicada")
print("Entrada:", 5, ",", 0)
print("Salida:", validarEntrada7(5, 0))
print("Entrada:", 2, ",", 4)
print("Salida:", validarEntrada7(2, 4))
print("Entrada:", 0, ",", 0)
print("Salida:", validarEntrada7(0, 0))
print("Entrada:", 5, ",", 3)
print("Salida:", validarEntrada7(5, 3))
print()

# Programa Principal reto 8
print("Reto 8: Determinar si un número es primo o no")
print("Entrada:", "sd")
n = validarEnteroNoNegativo("sd")
if n != None:
    print("Salida:", esNumeroPrimo(n))
print("Entrada:", -25)
n = validarEnteroNoNegativo(str(-25))
if n != None:
    print("Salida:", esNumeroPrimo(n))
print("Entrada:", 401)
print("Salida:", esNumeroPrimo(401))
print("Entrada:", 7)
print("Salida:", esNumeroPrimo(7))
print("Entrada:", 5)
print("Salida:", esNumeroPrimo(5))
print("Entrada:", 9)
print("Salida:", esNumeroPrimo(9))
print()

# Programa principal reto 9
#programa principal reto 9
print("reto 9: Sumar dígitos múltiplos")
print("reto 9 ")
print("entradas:",6,3)
print("salida: ",validarSumarDigitosMultiplos(6,3))
print("entradas:",1002,7)
print("salida: ",validarSumarDigitosMultiplos(1002,7))
print("entradas:",666,3)
print("salida: ",validarSumarDigitosMultiplos(666,3))
print("entradas:",1234,2)
print("salida: ",validarSumarDigitosMultiplos(1234,2))
print()

# Programa principal reto 10
print("Reto 10: Implementar una función iterativa en Python que reciba una cifra numérica y determine si es binaria o no")
print("Entrada:", "")
print("Salida:", validarEntrada10(""))
print("Entrada:", "23e")
print("Salida:", validarEntrada10("23e"))
print("Entrada:", 11001011)
print("Salida:", validarEntrada10(11001011))
print("Entrada:", 101601)
print("Salida:", validarEntrada10(101601))
print("Entrada:", 2)
print("Salida:", validarEntrada10(2))
print()

# Programa principal reto 11
print("Reto 11: Reciba una cifra numérica binaria y retorne su correspondiente representación decimal")
print("Entrada:", 121010)
n = validarBinario(str(121010))
if n != None:
    print("Salida: ", binarioADecimal(n))
print("Entrada:", 1010)
print("Salida:",binarioADecimal(1010))
print("Entrada:", 101)
print("Salida: ",binarioADecimal(101))
print("Entrada: ", 10000000)
print("Salida: ",binarioADecimal(10000000))
print("Entrada: ", 110010)
print("Salida: ",binarioADecimal(110010))
print()

#programa principal reto12
print("reto 12: Mostrar los años bisiestos.")
print("entradas:",2017,2019)
print("salida: ",validarMostrarAnnosBisiestos(2017,2019))
print("entradas:",2016,2019)
print("salida: ",validarMostrarAnnosBisiestos(2016,2019))
print("entradas:",2016,2021)
print("salida: ",validarMostrarAnnosBisiestos(2016,2021))
print("entradas:",2015,2024)
print("salida: ",validarMostrarAnnosBisiestos(2015,2024))
