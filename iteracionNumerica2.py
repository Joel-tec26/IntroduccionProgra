# Creado por: Joel Porras, Maria José Espinoza y Alexis Torres
# fecha de creación: 18/03/26 8:14am
# Ultima modificación: 19/03/2026 3:00pm
# version 3.14

# Definicion de funciones:
# Funciones generales: 

def esPar(pnum):
    """
    Funcionalidad:
    Comprueba si un npumero es par
    Entradas: 
    - pnum(int): número a valorar
    Salidas: 
    - Booleano indicando si es par o no 
    """
    if pnum%2==0:
        return True
    return False

def contarDigitos(pnum):
    """
    Funcionalidad:
    Cuenta los digitos de una cifra
    Entradas: 
    - pnum(int): número a valorar
    Salidas: 
    - La cantidad de digitos de la frase 
    """
    contador=0
    while pnum>0:
        contador+=1
        pnum//=10
    return contador

#reto 1
def obtenerPares(pnum):
    """
    Funcionalidad:
    Identifica los digitos pares de la frase
    Entradas: 
    - pnum(int): número a valorar
    Salidas: 
    - resultado(int): Los números pares de izquierda a derecha 
    """
    resultado=0
    contador=0
    digito=0
    while pnum>0:
        digito=pnum%10
        if esPar(digito):
            resultado+=digito*10**contador
            contador+=1
        pnum//=10
    return resultado

#reto 2
def esPalindromo(pnum):
    """
    Funcionalidad:
    Identifica si un número es palindromo o no 
    Entradas: 
    - pnum(int): número a valorar
    Salidas: 
    - Booleano indicando si es palindromo o no 
    """
    numOriginal=pnum
    reverso=0
    while pnum>0:
        digito=pnum%10
        reverso=reverso*10+digito
        pnum//=10
    return numOriginal==reverso

#reto 3
def formarNumeroInverso(pnum1,pnum2,pnum3):
    """
    Funcionalidad:
    cambia el orden de los digitos ingresados en la frase. Es decir su inverso
    Entradas: 
    - pnum1(int):  primer número en la frase original
    - pnum2(int):  segundo número en la frase original
    - pnum3(int):  tercer  número en la frase original
    Salidas: 
    - resultado(int): número inverso
    """
    resultado=pnum1+pnum2*10+pnum3*100
    return resultado
    
#reto 4
def obtenerCantidades(pnum):
    """
    Funcionalidad:
    Cuenta la cantidad de pares e impares en la frase 
    Entradas: 
    - pnum(int): número a valorar
    Salidas: 
    - pares(int): Devuelve la cantidad de pares en la frase
    - impares(int): Devuelve la cantidad de impares en la frase
    """
    pares=0
    impares=0
    while pnum>0:
        if esPar(pnum%10):
            pares+=1
        else:
            impares+=1
        pnum//=10
    return pares, impares

#reto 5
def convertirABinario(pnum):
    """
    Funcionalidad:
    Convierte un numero base 10 a binario
    Entradas: 
    - pnum(int): número a valorar
    Salidas: 
    - binario(int): Número binario correspondiente a la base 10
    """
    binario = 0
    colocador = 1

    while pnum > 0:
        residoBi = pnum % 2
        binario = residoBi * colocador + binario
        colocador *= 10
        pnum //= 2
    return binario

#reto 6
def convertirAOctal(pnum):
    """
    Funcionalidad:
    Convierte un numero base 10 a octaval 
    Entradas: 
    - pnum(int): número a valorar
    Salidas: 
    - octal(int): Número octaval correspondiente a la base 10
    """
    octal=0
    colocador = 1
    while pnum>0:
        residuoOc = pnum % 8
        octal = residuoOc * colocador + octal
        colocador *= 10
        pnum //= 8
    return octal

#reto 7
def compararNumeros(pnum1,pnum2):
    """
    Funcionalidad:
    Compara si los dos números son iguales (digito por digito)
    Entradas: 
    - pnum1(int): número 1 a valorar
    - pnum2(int): número 1 a valorar
    Salidas: 
    - texto mencionando si son iguales o no
    """
    digito1=pnum1%10
    digito2=pnum2%10
    while digito1>0 and digito2>0:
        digito1=pnum1%10
        digito2=pnum2%10
        if digito1!=digito2:
            return "los números no son iguales"
        pnum1//=10
        pnum2//=10
    return "los números son iguales"

#reto 8
def diferenciarNumeros (pnum1, pnum2):
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

    resultado = 0
    colocador = 1

    while pnum1 > 0:
        digito1 = pnum1 % 10
        temporal = pnum2
        encontrado = False
        while temporal > 0:
            if digito1 == temporal % 10:
                encontrado = True
            temporal //= 10
        if not encontrado:
            resultado = digito1 * colocador + resultado
            colocador *= 10
        pnum1 //= 10
    if resultado==0:
        return False
    return resultado

#reto 9
def verificarParidad(pnum,pposicion):
    """
    Funcionalidad:
    Determinar si el dígito que está en la posición “x” de un número “n” es par
    Entradas: 
    - pnum1(int): frase de digitos a evaluar 
    - pposicion(int): posición del digito en la frase a evaluar 
    Salidas: 
    - booleano indicando si es par o no
    """
    if esPar(pnum//10**(pposicion-1)):
        return True
    return False

#reto 10
def repetirDigito(pdigito,pnum,prepeticiones):
    """
    Funcionalidad:
    Construye un nuevo número reemplazando cada aparición de un dígito específico 
    por una secuencia del mismo dígito repetida n veces, donde n es el valor del tercer parámetro. 
    Mantiene el orden original de los demás dígitos.
    Entradas: 
    - pnum(int): número original a analizar.
    - pdigito(int): El dígito que se desea repetir
    -prepeticiones(int): La cantidad de veces que aparecerá el dígito en el resultado
    Salidas: 
    - resultado(int): El nuevo número formado con las repeticiones aplicadas
    """
    resultado=0
    numDigitos=contarDigitos(pnum)
    digito=0 
    while numDigitos>0:
        digito=(pnum%10**numDigitos)//10**(numDigitos-1)
        if digito==pdigito:
            cont=0
            while prepeticiones>cont:
                resultado*=10
                resultado+=pdigito
                cont+=1
        else:
            resultado*=10
            resultado+=digito
        numDigitos-=1
    return resultado

#programa principal

# reto 1
print("reto 1: Obtener pares en el mismo orden")
print("entrada:",876543)
print("salida:",obtenerPares(876543))
print("entrada:",1273423)
print("salida:",obtenerPares(1273423))
print("entrada:",45678)
print("salida:",obtenerPares(45678))
print()

# reto 2
print("reto 2: Numero Palíndromo")
print("entrada:",161)
print("salida:",esPalindromo(161))
print("entrada:",2992)
print("salida:",esPalindromo(2992))
print("entrada:",3003)
print("salida:",esPalindromo(3003))
print("entrada:",2882)
print("salida:",esPalindromo(2882))
print("entrada:",28821)
print("salida:",esPalindromo(28821))
print("entrada:",128821)
print("salida:",esPalindromo(128821))
print("entrada:",61)
print("salida:",esPalindromo(61))
print("entrada:",66)
print("salida:",esPalindromo(66))
print("entrada:",660)
print("salida:",esPalindromo(660))
print()

# #reto 3
print("reto 3: Formar un número en orden inverso")
print("entrada:",4,6,5)
print("salida:",formarNumeroInverso(4,6,5))
print("entrada:",0,0,1)
print("salida:",formarNumeroInverso(0,0,1))
print("entrada:",1,0,0)
print("salida:",formarNumeroInverso(1,0,0))
print()

# #reto 4
print("reto 4: cantidad de pares e impares")
print("entrada:",876543)
print("salida:",obtenerCantidades(876543))
print("entrada:",1273423)
print("salida:",obtenerCantidades(1273423))
print("entrada:",45678)
print("salida:",obtenerCantidades(45678))
print("entrada:",7)
print("salida:",obtenerCantidades(7))
print()

# #reto 5
print("reto 5: convertir a binario")
print("entrada:",10)
print("salida",convertirABinario(10))
print("entrada:",125)
print("salida",convertirABinario(125))
print()

# #reto 6
print("reto 6: convertir a octal")
print("entrada:",786)
print("salida:",convertirAOctal(786))
print("entrada:",199)
print("salida:",convertirAOctal(199))
print("entrada:",19782)
print("salida:",convertirAOctal(19782))
print()

#reto 7
print("reto 7: compare si 2 números son iguales")
print("entrada:",4356,4356)
print("salida:",compararNumeros(4356,4356))
print("entrada:",6987,5987)
print("salida:",compararNumeros(6987,5987))
print("entrada:",0,0)
print("salida:",compararNumeros(0,0))
print()

#reto 8
print("reto 8: diferencia de dígitos entre 2 números")
print("entrada:",29837,321)
print("salida:",diferenciarNumeros(29837,321))
print("entrada:",29837,321)
print("salida:",diferenciarNumeros(23,3218))
print("entrada:",29837,321)
print("salida:",diferenciarNumeros(6328,6817))
print()

#reto 9
print("reto 9: verificar paridad")
print("entrada:",12521,3)
print("salida:",verificarParidad(12521,3))
print("entrada:",12481,4)
print("salida:",verificarParidad(12481,4))
print()

#reto 10
print("reto 10: repetir un numero n cantidad de veces")
print("entrada:",4,124564583,2)
print("alida:",repetirDigito(4,124564583,2))
print("entrada:",1,18117,3)
print("salida:",repetirDigito(1,18117,3))