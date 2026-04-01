# Creado por: Joel Jesús Porras Muñoz
# Fecha de creación: 11/3/2026 18:10pm
# Ultima modificación: 11/3/2026 19:12pm
# Versión 3.14.3

#definición de funciones
def identificarMayor (pnum1, pnum2, pnum3):
    """
    Funcionalidad: 
    Determina cuál de tres números es el mayor o si algunos o todos son iguales

    entradas:
    -pnum1(float): número 1 digitado
    -pnum2(float): número 2 digitado
    -pnum3(float): número 3 digitado

    salidas
    -mensaje con el resultado (str)
    """
    if pnum1>pnum2:
        if pnum1>pnum3:
            return "El numero: "+str(pnum1)+" es el mayor"
        else:
            if pnum1==pnum3:
                return "Los números: "+str(pnum1)+" y "+str(pnum3)+" son los mayores"
            else:
                return "El número: "+str(pnum3)+" es el mayor"
    else:
        if pnum1 ==pnum2:
            if pnum1>pnum3:
                return "Los números: "+str(pnum1)+" y "+str(pnum2)+" son los mayores"
            else:
                if pnum1==pnum3:
                    return "Los números: "+str(pnum1)+", "+str(pnum2)+" y "+str(pnum3)+" son iguales"
                else:
                    return "El número: "+str(pnum3)+" es el mayor"
        else:
            if pnum2>pnum3:
                return "El número: "+str(pnum2)+" es el mayor"
            else:
                if pnum2==pnum3:
                    return "Los números: "+str(pnum2)+" y "+str(pnum3)+" son los mayores"
                else:
                    return "El número: "+str(pnum3)+" es mayor"

# Programa Principal

# Llamada 1
num1 = float(input("Ingrese número 1: "))
num2 = float(input("Ingrese número 2: "))
num3 = float(input("Ingrese número 3: "))
resultado = identificarMayor(num1, num2, num3)
print(resultado)

# Llamada 2
num1 = float(input("Ingrese número 1: "))
num2 = float(input("Ingrese número 2: "))
num3 = float(input("Ingrese número 3: "))
print(identificarMayor(num1, num2, num3))

# llamada 3
print(identificarMayor(pnum1 = 80, pnum2=85, pnum3=90))
