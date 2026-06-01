#
#
#
#

# reto 1

def sumarAux(actual, limite, sumaParcial):
    if actual > limite:
        return print(sumaParcial)
    if actual % 2 != 0:
        nuevoAcumulador = sumaParcial + actual
    else:
        nuevoAcumulador = sumaParcial
    return sumarAux(actual + 1, limite, nuevoAcumulador)


def sumarNumerosImparesEnIntervalo(A, B):
    if not isinstance(A, int) or not isinstance(B, int):
        return print('A y B debe ser numero enteros')
    if B < A:
        return print('B debe ser mayor o igual a A')
    return sumarAux(A, B, 0)

# reto 2

def obtenerSumCuadradosAux(actual, limite, sumaParcial):
    if actual > limite:
        return print(sumaParcial)
    nuevoAcumulador = sumaParcial + (actual ** 2)
    return obtenerSumCuadradosAux(actual + 1, limite, nuevoAcumulador)

def obtenerSumCuadrados(m, n):
    if not isinstance(m, int) or not isinstance(n, int):
        return print(-1)
    if n < m:
        return print(-1)
    return obtenerSumCuadradosAux(m, n, 0)

# reto 3

def obtenerParesImparesAux(numero, pares, impares):
    if numero == 0:
        return print((pares, impares))
    ultimoDigito = numero % 10
    if ultimoDigito % 2 == 0:
        nuevosPares = pares + 1
        nuevosImpares = impares
    else:
        nuevosPares = pares
        nuevosImpares = impares + 1
    return obtenerParesImparesAux(numero // 10, nuevosPares, nuevosImpares)

def obtenerParesImpares(numero):
    if type(numero) is not int:
        return print(())
    if numero == 0:
        return print((1, 0))
    numeroAbsoluto = abs(numero)
    return obtenerParesImparesAux(numeroAbsoluto, 0, 0)

# reto 4

def esBinarioAux(numero):
    if numero == 0:
        return print(True)
    ultimoDigito = numero % 10
    if ultimoDigito != 0 and ultimoDigito != 1:
        return print(False)
    return esBinarioAux(numero // 10)

def esBinario(numero):
    if type(numero) is not int:
        print(False)
    if numero == 0:
        return print(True)
    numeroAbsoluto = abs(numero)
    return esBinarioAux(numeroAbsoluto)

# reto 5
def contarBisiestosAux(actual, limite, contadorParcial):
    if actual > limite:
        print(contadorParcial)
        return
    p = (actual % 4 == 0)
    noQ = (actual % 100 != 0)
    r = (actual % 400 == 0)
    if p and (noQ or r):
        nuevoContador = contadorParcial + 1
    else:
        nuevoContador = contadorParcial
    return contarBisiestosAux(actual + 1, limite, nuevoContador)

def contarBisiestos(añoInicial, añoFinal):
    if type(añoInicial) is not int or type(añoFinal) is not int:
        print("Los años deben ser números enteros positivos mayores que 0.")
        return 
    if añoInicial <= 0 or añoFinal <= 0:
        print("Los años deben ser números enteros positivos mayores que 0.")
        return 
    if añoInicial >= añoFinal:
        print("El año inicial debe ser debe ser menor que el año final.")
        return 
    return contarBisiestosAux(añoInicial, añoFinal, 0)

# reto 6

def colonizarAux(generacionActual, generacionLimite, habitantesAcumulados):
    if generacionActual == generacionLimite:
        print(habitantesAcumulados)
        return 
    nuevosHabitantes = (habitantesAcumulados // 2) * 3
    return colonizarAux(generacionActual + 1, generacionLimite, nuevosHabitantes)

def colonizar(generacion):
    if type(generacion) is not int:
        print ("Debe indicar un número mayor o igual que cero únicamente.")
        return
    if generacion < 0:
        print ("Debe indicar un número mayor o igual que cero únicamente.")
        return
    return colonizarAux(0, generacion, 27)



# menu principal
print("reto 1")
sumarNumerosImparesEnIntervalo("Hola", 25.3)
sumarNumerosImparesEnIntervalo(5, 0)
sumarNumerosImparesEnIntervalo(-5, 5)
sumarNumerosImparesEnIntervalo(0, 7)
sumarNumerosImparesEnIntervalo(2, 125)
print()

print("reto 2")
obtenerSumCuadrados(4, 7)
obtenerSumCuadrados(7, 4)
obtenerSumCuadrados(4.5, 7)
obtenerSumCuadrados(1, 5)
print()

print("reto 3")
obtenerParesImpares(3214)
obtenerParesImpares(-18006)
obtenerParesImpares(0)
obtenerParesImpares(1)
obtenerParesImpares("abc")
print()

print("reto 4")
esBinario(1001019)
esBinario(5679)
esBinario(0)
esBinario(10101)
print()

print("reto 5")
contarBisiestos(1500, 1836)
contarBisiestos(2000, 2025)
contarBisiestos(2022, 2023)
contarBisiestos(2023, 2020)
print()

print("reto 6")
colonizar(0)
colonizar(1)
colonizar(2)
colonizar(5)
colonizar(7)
colonizar("7")