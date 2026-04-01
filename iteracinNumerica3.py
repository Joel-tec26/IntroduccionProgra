#
#
#
#

#definicion de funciones
#reto1

def esPerfeto (pnum):
    suma=0
    for i in range (1, pnum):
        if pnum%i==0:
            suma+=i
    return suma==pnum

# reto 2
def obtenerMCD (N, M):
    while M!= 0:
        residuo = N % M
        N = M
        M = residuo
    return N

# reto 3
def obtenerMCM(N, M):   
    if N == 0 or M == 0:
        return 0 
    multiplicacion = N * M
    mcd = obtenerMCD(N, M)
    resultado = multiplicacion // mcd
    return resultado

# reto 4
def esBisiesto(aaaa):
    return (aaaa % 4 == 0 and aaaa % 100 != 0) or (aaaa % 400 == 0)

def validarFecha(fecha):
    # Ejemplo: 30032015
    dia = fecha // 1000000          # Obtiene los primeros dos dígitos (30)
    mes = (fecha // 10000) % 100    # Obtiene los dígitos del medio (03)
    anno = fecha % 10000            # Obtiene los últimos cuatro dígitos (2015)

    if anno < 1800:
        return False
    if mes < 1 or mes > 12:
        return False
    if mes in [1, 3, 5, 7, 8, 10, 12]:
        diasMaximos= 31
    elif mes in [4, 6, 9, 11]:
        diasMaximos= 30
    elif mes == 2:
        if  esBisiesto(anno):
            diasMaximos = 29
        else:
            diasMaximos = 28
    if dia < 1 or dia > diasMaximos:
        return False
    return True

# programa principal
# reto1 
print ("Entrada: 6")
print("salida: ", esPerfeto(6))
print()

# reto 2
print("El MCD entre 12 y 69 es ", obtenerMCD(12, 69))
print("El MCD entre 12 y 60 es ", obtenerMCD(12, 60))
print("El MCD entre 48 y 36 es ", obtenerMCD(48, 36))

# reto 3
print("El mcm entre 12 y 69 es: ", obtenerMCM(12, 69))
print("El mcm entre 12 y 60 es: ", obtenerMCM(12, 60))
print("El mcm entre 48 y 36 es: ", obtenerMCM(48, 36))
print()

# reto 4
print("Resultado para 30032015:", validarFecha(30032015)) 
print("Resultado para 31092006:", validarFecha(31092006)) 
print("Resultado para 29022015:", validarFecha(29022015))