# Creado por: Joel Jesús Porras Muñoz, Alexis Torres y María Jose Espinoza 
# Fecha de creación: 21/04/2026 9:30am
# Ultíma modificación: 25/4/2026 11am
# Versión: 3.14

#definicion de funciones

def esPar(pnum):
    """
    Funcionalidad:
    Determina si un número es par
    Entradas:
    -pnum(int): número entero a evaluar
    Salidas:
    -resultado(bool): True si el número es par, False si es impar
    """
    return pnum%2==0

def esPalindromo(palabra):
    """
    Funcionalidad:
    Verifica si una palabra es un palíndromo
    Entradas:
    -palabra(str): palabra a evaluar
    Salidas:
    -resultado(bool): True si es palíndromo y tiene más de un carácter, False en caso contrario
    """
    palabra = palabra.lower()
    return len(palabra) > 1 and palabra == palabra[::-1]

def esInfinitivo(palabra):
    """
    Funcionalidad:
    Determina si una palabra corresponde a un verbo en infinitivo según su terminación
    Entradas:
    -palabra(str): palabra a evaluar
    Salidas:
    -resultado(bool): True si termina en ar, er, ir, or o ur; False en caso contrario
    """
    terminaciones = ('ar', 'er', 'ir', 'or', 'ur')
    return palabra.lower().endswith(terminaciones)

def contarParesImpares(ptupla):
    """
    Funcionalidad:
    Cuenta la cantidad de números pares e impares dentro de una tupla,
    validando que cada número sea natural de 4 dígitos
    Entradas:
    -ptupla(tuple): tupla de números enteros a evaluar
    Salidas:
    -resultado(tuple): cantidad de números pares e impares
    -mensaje(str): mensaje de error si algún número no cumple la condición
    """
    pares=0
    impares=0
    for i in ptupla:
        if i//1000>=0 and i//1000<10:
            if esPar(i):
                pares+=1
            else:
                impares+=1
        else:
            return "Debe ser un número natural de 4 dígito"
    return (pares,impares)

def separarParesImpares(ptupla):
    """
    Funcionalidad:
    Separa los números pares e impares de una tupla en dos listas,
    validando que cada número sea natural de 4 dígitos.
    Entradas:
    -ptupla(tuple): tupla de números enteros a evaluar
    Salidas:
    -resultado(tuple): dos listas, una con números pares y otra con impares
    -mensaje(str): mensaje de error si algún número no cumple la condición
    """
    pares=[]
    impares=[]
    for i in ptupla:
        if i//1000>=0 and i//1000<10:
            if esPar(i):
                pares.append(i)
            else:
                impares.append(i)
        else:
            return "Debe ser un número natural de 4 dígito"
    return (pares,impares)

def categorizarPalabras(ptupla):
    """
    Funcionamiento: Recorre una tupla de frases y clasifica cada palabra
    limpia en dos listas: una con verbos en infinitivo y otra con palíndromos.
    Entradas:
    - ptupla(tuple): tupla de frases de texto a analizar
    Salidas:
    - resultado(list): lista con dos sublistas [infinitivos, palindromos]
    - mensaje(str): mensaje de error si la entrada no es una tupla
    """

    if not type(ptupla)==tuple:
        return "Debe ingresar una tupla obligatoriamente"
    infinitivos = []
    palindromos = []
    for frase in ptupla:
        palabras=frase.lower().split()
        for i in palabras:
            palabraLimpia=i.strip(",.-_:;´+}¨*]{[!#$%&/()=?'¿¡|°")
            if esInfinitivo(palabraLimpia):
                infinitivos.append(palabraLimpia)
            if esPalindromo(palabraLimpia):
                palindromos.append(palabraLimpia)
    return [infinitivos,palindromos]

def esNumPerfeto (pnum):
    """
    Funcionamiento: Determina si un número es perfecto, es decir, si la suma
    de sus divisores propios es igual al número mismo.
    Entradas:
    - pnum(int): número entero a evaluar
    Salidas:
    - resultado(bool): True si el número es perfecto, False en caso contrario
    """
    suma=0
    for i in range (1, pnum):
        if pnum%i==0:
            suma+=i
    return suma==pnum

def esNumPerfectoAux(ptupla):
    """
    Funcionamiento: Recibe una tupla de exactamente 5 números y retorna
    una lista con aquellos que sean números perfectos.
    Entradas:
    - ptupla(tuple): tupla con exactamente 5 valores enteros a analizar
    Salidas:
    - resultado(list): lista con los números perfectos encontrados
    - mensaje(str): mensaje de error si la tupla no tiene 5 elementos
     o si no se encuentran números perfectos
    """
    resultado=[]
    if len(ptupla)==5:    
        for i in ptupla:
            if esNumPerfeto(i):
                resultado.append(i)
        if resultado==[]:
            return "no hay números perfectos"
    else:
        return "debe indicar exactamente 5 valores de entrada para analizar"
    return resultado

def obtenerDiferencia(pnum1, pnum2):
    """
    Funcionalidad:
    retorna un número formado por los dígitos que están en el primer número 
    pero no aparecen en el segundo número, manteniendo el orden original
    Entradas: 
    - pnum1(int): número 1 a valorar
    - pnum2(int): número 2 a valorar
    Salidas: 
    - resultado(int): número quitando los digitos de pnum2
    -False(bool): indicando que no hay números que se repitan 
    """
    cadena1=str(pnum1)
    cadena2=str(pnum2)
    resultadoFinal=""
    for digitoActual in cadena1:
        if digitoActual not in cadena2 and digitoActual not in resultadoFinal:
            resultadoFinal+=digitoActual
    for digitoActual in cadena2:
        if digitoActual not in cadena1 and digitoActual not in resultadoFinal:
            resultadoFinal+=digitoActual
    if resultadoFinal=="":
        return False
    return int(resultadoFinal)

def obtenerDiferenciaAux(ptupla):
    """
    Funcionamiento: Valida que la entrada sea una tupla con dos enteros
    positivos y delega el cálculo a obtenerDiferencia.
    Entradas:
    - ptupla(tuple): tupla con dos valores enteros positivos a comparar
    Salidas:
    - resultado(int): número con los dígitos no compartidos entre ambos
    - False(bool): si todos los dígitos son compartidos
    - mensaje(str): mensaje de error según el tipo de validación fallida
    """

    if type(ptupla)!=tuple:
        return "Debe recibir una tupla para analizar los valores"
    num1=ptupla[0]
    num2=ptupla[1]
    if type(num1)!=int or type(num2)!=int:
        return "Ambos valores deben ser enteros"
    if 0>num1 or 0>num2:
        return "Ambos valores deben ser mayores a 0"
    return obtenerDiferencia(num1, num2)

def esParAmigable(ptupla):
    """
    Funcionamiento: Determina si dos números forman un par amigable, es decir,
    si la suma de los divisores propios de cada uno es igual al otro número.
    Entradas:
    - ptupla(tuple): tupla con dos valores enteros a evaluar
    Salidas:
    - resultado(bool): True si forman un par amigable, False en caso contrario
    """
    suma1=0
    suma2=0
    num1=ptupla[0]
    num2=ptupla[1]
    if num1==num2:
        False
    for i in range(1, num1):
        if num1%i==0:
            suma1+=i
    for i in range(1, num2):
        if num2%i==0:
            suma2+=i
    if suma1==num2 and suma2==num1:
        return True
    return False


#programa principal

print("reto1")
print(contarParesImpares((1235, 1742, 1111, 2321)))
print(contarParesImpares((2426,1224,1542,1000)))
print(contarParesImpares((3557,1237,1243)))
print(contarParesImpares((219999,)))
print()
print("reto3")
print(separarParesImpares((1235, 1742, 1111, 2321)))
print(separarParesImpares ((2426,1224,1542,1000)))
print(separarParesImpares ((3557,1237,1243,4561)) )
print(separarParesImpares((3557,)) )
print(separarParesImpares((219999,)))
print()
print("reto5")
print(esNumPerfectoAux((6,123,45,496,17)))
print(esNumPerfectoAux((100,15,28,51,4)))
print(esNumPerfectoAux((8128,75,28,12,1000)))
print(esNumPerfectoAux((750,122,14,3,1550)))
print(esNumPerfectoAux((10,23,33550336,125,750)))
print(esNumPerfectoAux((2,)))
print()
print("reto7")
print(categorizarPalabras(("Cantar llorar y reír que más pedir a la vida","Reconocer las salas del museo es bueno")))
print(categorizarPalabras(("Ana tiene su radar en el ojo siempre",)))
print(categorizarPalabras(("Equivocarse es de humanos",)))
print(categorizarPalabras("Equivocarse es de humanos"))
print()
print("reto9")
print(obtenerDiferenciaAux((1265, 42)))
print(obtenerDiferenciaAux((8587, 71457)))
print(obtenerDiferenciaAux((542, 254)))
print(obtenerDiferenciaAux((2984, 48298)))
print(obtenerDiferenciaAux((12345, 67890)))
print(obtenerDiferenciaAux((1, 1010)))
print(obtenerDiferenciaAux((-21, 1010)))
print(obtenerDiferenciaAux((1, 1010.6)))
print(obtenerDiferenciaAux([12345, 67890]))
print()
print("reto11")
print(esParAmigable((220, 284)))
print(esParAmigable((15, 18)))
print(esParAmigable((1210, 1184)) )
print(esParAmigable((890, 890)))