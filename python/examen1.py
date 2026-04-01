#Creado por: Joel Jesús Porras Muñoz
# Fecha de creación: 27/03/2026 8:00am
# Ultima modificación: 27/03/2026 20:14pm
# versión: 3.14

# Reto 1
# definición de funciones 

def contarDigitos(pnum):
    """
    Funcionalidad: cuenta la cantidad de digitos de la frase númerica
    Entradas: 
    -pnum(int): frase numerica a valorar
    Salidas:
    -cont(int): cantidad de digitos en la frase númerica
    """
    cont=1
    if pnum==0:
        cont+=1
        return cont
    while pnum>0:
        cont+=1
        pnum//=10
    return cont

def esPar (pnum):
    """
    Funcionalidad: Valora si un nímero es par 
    Entradas: 
    -pnum(int): número a valorar
    Salidas:
    -booleanos indcando si es par(True) o no(False)
    """
    if pnum%2==0:
        return True
    else:
        return False 
    
def esImparEnRango (pinicial, pfinal, pnum):
    """
    Funcionalidad: Evalúa si todos los dígitos de un número dentro de un rango específico de posiciones son impares. Extrae ese 
    segmento del número y verifica dígito por dígito
    Entradas:

    -pinicial (int): posición inicial del rango
    -pfinal (int): posición final del rango
    -pnum (int): número del cual se van a analizar los dígitos
    Salidas:
    -True (bool): si todos los dígitos en el rango son impares.
    -False (bool): si al menos uno de los dígitos es par.
    """
    totalDig=contarDigitos(pnum)
    potencia = totalDig - pfinal
    temp = pnum // (10 ** potencia)
    temp = temp % (10 ** (pfinal - pinicial + 1))
    while temp>0: 
        dig = temp % 10
        if dig % 2 == 0:
            return False
        temp //= 10
    return True

def esImparEnRangoaux (pinicial, pfinal, pnum):
    """
    Funcionalidad:
    valida los datos de entrada (rangos y número) y luego utiliza la función 
    esImparEnRango para determinar si los dígitos en el rango son impares.
    Entradas: 
    -pinicial (int): posición inicial del rango.
    -pfinal (int): posición final del rango.
    -pnum (int): número a evaluar.
    Salidas:
    str que devuelve errores:
    -"Debe indicar valores numéricos para los rangos."
    -"Los valores de los rangos deben ser mayores o iguales a 1."
    -"El primer rango debe ser menor al segundo."
    -"En la cifra recibida no es posible obtener ese índice."
    str que devuelve resultados de la evaluación:
    -"Los números del rango SON impares."
    -"Los números del rango NO son impares."


    """
    if type(pinicial)!= int or type(pfinal) != int:
        return "Debe indicar valores numéricos para los rangos."
    elif pinicial ==0 or pfinal==0:
        return "Los valores de los rangos deben ser mayores o iguales a 1."
    elif pfinal < pinicial:
        return "El primer rango debe ser menor al segundo."
    totalDig=contarDigitos(pnum) 
    if pfinal>totalDig:
        return "En la cifra recibida no es posible obtener ese índice."
    resultado= esImparEnRango(pinicial, pfinal, pnum)
    if resultado==True:
        return "Los números del rango SON impares."
    else: 
        return "Los números del rango NO son impares."
    
# Programa Principal Reto1

print(esImparEnRangoaux (0,2,12522))
print(esImparEnRangoaux (4,2,1242))
print(esImparEnRangoaux ("uno",2,1242))
print(esImparEnRangoaux (1,8,1242))
print(esImparEnRangoaux (1,3,1242))
print(esImparEnRangoaux(1,3,1735))
print(esImparEnRangoaux(3,6,1723521))
print()

#Reto 2

# definición de funciones
def multiplicarDig (num1, num2):
    """
    Funcionalidad: Multiplica los dígitos de num1 y num2 posición por posición
    Entradas:
    -num1(int): frase númerica 1 a valorar
    -num2(int): frase númerica 2 a valorar
    Salidas:
    -resultado (int): Valor compuesto por los residuos de las multiplicaciones individuales
    """
    cont=0
    resultado=0
    while num1>0 and num2>0:
        temp1=num1%10
        temp2=num2%10
        multiplicacion=temp1*temp2
        resultado=((multiplicacion%10)*10**cont)+resultado 
        num1//=10
        num2//=10
        cont+=1
    return resultado

def multiplicarDigaux(num1, num2):
    """
    Funcionalidad: actúa como validador de longitud de digitos
    Entradas:
    -num1(int): frase númerica 1 a valorar
    -num2(int): frase númerica 2 a valorar
    Salidas:
    int: el número procesado si las longitudes coinciden
    str: mensaje de error si las longitudes son distintas
    """
    totalNum1=contarDigitos(num1)
    totalNum2=contarDigitos(num2)
    if totalNum1!=totalNum2:
        return "Los números de entrada deben poseer la misma cantidad de dígitos."
    else:
        return multiplicarDig(num1, num2)

# Programa pruncipal reto 2
    
print(multiplicarDigaux(240,42))
print(multiplicarDigaux(323,388))
print(multiplicarDigaux(24,42))
print(multiplicarDigaux(153,632))
print()

# reto 3

# definición de funciones

def definirIgualdad(pnum1, pnum2):
    """
    Funcionalidad: determina si todos los dígitos presentes en pnum2 existen al menos una vez dentro de pnum1
    Entradas:
    -pnum1 (int): número que sirve como base de búsqueda
    -pnum2(int): frase númerica que se va a verificar
    Salidas:
    True (bool): si cada dígito de pnum2 se encuentra contenido en pnum1
    -False (bool): si al menos un dígito de pnum2 no existe en pnum1
    """
    temp2 = pnum2
    while temp2 > 0:
        dig2 = temp2 % 10
        temp2 //= 10
        temp1 = pnum1
        resultado = False
        while temp1 >0:
            dig1= temp1 % 10
            if dig1 == dig2:
                resultado = True
                break
            temp1//= 10
        if not resultado:
            return False
    return True
    
# Programa Principal

print(definirIgualdad (62841, 14682))
print(definirIgualdad (62841, 362841))
print(definirIgualdad (82614, 62841))
print(definirIgualdad (64812, 81624))
print(definirIgualdad (1029, 108))


# Me di cuenta de errores comunes que tal vez no se ven en papel como tal, y entiendo la importancia de llevar un orden estructurado.
#  Me sirvio para compreder varias cosas 