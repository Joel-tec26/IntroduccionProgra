# creador por: Joel Porras
# Fecha de creación: 28/5/2026  7pm
# ultima modificacion: 28/5/2026 10om
# versión: 3.14

# reto 3
def validarEntero(pNum):
    return type(pNum) == int

def sumarDigitos(pNum):
    if pNum == 0:
        return 0
    else:
        return (pNum % 10) + sumarDigitos(pNum // 10)

def sumarDigitosAux(pNum):
    if validarEntero(pNum):
        resultado = sumarDigitos(abs(pNum))
        return f"La suma es de: {resultado}"
    else:
        return "El valor ingresado debe corresponder a un número entero únicamente."

# reto 4

def validarNumero(pNum):
    return type(pNum) == int

def multiplicarImpares(pNum):
    if pNum == 0:
        return -1
    digito = pNum % 10
    resto = multiplicarImpares(pNum // 10)
    if digito % 2 != 0:
        if resto == -1:
            return digito
        else:
            return digito * resto
    else:
        return resto

def multiplicarImparesAux(pNum):
    if validarNumero(pNum):
        if pNum == 0:
            return "La multiplicación impar es: 0"
        resultado = multiplicarImpares(abs(pNum))
        if resultado == -1:
            resultado = 0
        return f"La multiplicación impar es: {resultado}"
    else:
        return "El valor ingresado debe corresponder a un número únicamente."

# Reto 5
def mayorDigito(pNum):
    if pNum == 0:
        return 0
    digito = pNum % 10
    resto = mayorDigito(pNum // 10)
    if digito > resto:
        return digito
    else:
        return resto

def mayorDigitoAux(pNum):
    if validarNumero(pNum):
        if pNum == 0:
            return "El más grande es: 0"
        resultado = mayorDigito(abs(pNum))
        return f"El más grande es: {resultado}"
    else:
        return "El valor ingresado debe corresponder a un número únicamente."

# Reto 7
def formarNumero(pNum):
    if pNum == 0:
        return 0
    digito = pNum % 10
    resto = formarNumero(pNum // 10)
    if digito % 2 == 0:
        return (resto * 10) + digito
    else:
        return resto

def formarNumeroAux(pNum):
    if validarEntero(pNum):
        if pNum == 0:
            return 0
        return formarNumero(abs(pNum))
    else:
        return 'El numero debe ser entero'

# reto 8
def validarEnterosPositivos(pBase, pExponente):
    return (type(pBase) == int and pBase >= 0 and 
            type(pExponente) == int and pExponente >= 0)

def elevar(pBase, pExponente):
    if pExponente == 0:
        return 1
    else:
        return pBase * elevar(pBase, pExponente - 1)

def elevarAux(pBase, pExponente):
    if validarEnterosPositivos(pBase, pExponente):
        return elevar(pBase, pExponente)
    else:
        return "Ambos parámetros deben ser enteros positivos mayores o iguales que cero."

# reto 10
def validarEntradas(pNum, pDigito):
    return (type(pNum) == int and pNum > 0 and type(pDigito) == int and pDigito > 0)

def sumarDigitosMultiplos(pNum, pDigito):
    if pNum == 0:
        return 0
    digitoActual = pNum % 10
    restoMúltiplos = sumarDigitosMultiplos(pNum // 10, pDigito)
    if digitoActual % pDigito == 0:
        return digitoActual + restoMúltiplos
    else:
        return restoMúltiplos

def sumarDigitosMultiplosAux(pNum, pDigito):
    if validarEntradas(pNum, pDigito):
        return sumarDigitosMultiplos(pNum, pDigito)
    else:
        return "El número debe ser un entero positivo mayor que cero."


# programa principal
print("Reto 3")
print("Entrada:", 12345)
print(sumarDigitosAux(12345))
print("Entrada:", 12.5)
print(sumarDigitosAux(12.5))
print()

print("Reto 4")
print("Entrada: 123a.  Salida: ", multiplicarImparesAux("123a"))
print("Entrada: 12345.  Salida: ", multiplicarImparesAux(12345))
print("Entrada: 246.  Salida: ", multiplicarImparesAux(246))
print("Entrada: 1246.  Salida: ", multiplicarImparesAux(1246))
print()

print("Reto 5")
print("Entrada: '123a'.  Salida: ", mayorDigitoAux("123a"))
print("Entrada: 4571.  Salida: ", mayorDigitoAux(4571))
print("Entrada: 333.  Salida: ", mayorDigitoAux(333))
print()

print("Reto 7")
print("Entrada: Hola!.  Salida: ", formarNumeroAux("Hola!"))
print("Entrada: 255.3.  Salida: ", formarNumeroAux(255.3))
print("Entrada: -2556.  Salida: ", formarNumeroAux(-2556))
print("Entrada: 2552180.  Salida: ", formarNumeroAux(2552180))
print("Entrada: 125.  Salida: ", formarNumeroAux(125))
print("Entrada: 135.  Salida: ", formarNumeroAux(135))
print()

print("Reto 8")
print("Entrada: 5, 0.  Salida: ", elevarAux(5, 0))
print("Entrada: 2, 4.  Salida: ", elevarAux(2, 4))
print("Entrada: 0, 0.  Salida: ", elevarAux(0, 0))
print("Entrada: 5, 3.  Salida: ", elevarAux(5, 3))
print("Entrada: 5, -2.  Salida: ", elevarAux(5, -2))
print()

print("Reto 10")
print("Entrada: 6, 3.  Salida: ", sumarDigitosMultiplosAux(6, 3))
print("Entrada: 1002, 7.  Salida: ", sumarDigitosMultiplosAux(1002, 7))
print("Entrada: 666, 3.  Salida: ", sumarDigitosMultiplosAux(666, 3))
print("Entrada: 1234, 2.  Salida: ", sumarDigitosMultiplosAux(1234, 2))
print("Entrada: -50, 2.  Salida: ", sumarDigitosMultiplosAux(-50, 2))




