#
#
#
#

# definicion de funciones
# Reto 3 stringv2
def invertirPalabras (ptexto):
    
    biblioteca = "aáAeéEiíIoóOUuúü"
    if ptexto=="0":
        return ""
    if ptexto[-1] in biblioteca:
        resultado=""
        indice =-1
        while indice >= -len(ptexto):
            letra= ptexto[indice]
            resultado+= letra
            indice-=1
        print (resultado)

    return invertirPalabras(input("ingrese una palabra: "))

# Reto 5 stringv2
import time
from datetime import date
def obtenerFecha():
    hoy=date.today()
    return str(hoy)

def calcularEdad (pfecha1, pfecha2):
    anno1=int(pfecha1[:4])
    anno2=int(pfecha2[:4])
    mes1= int(pfecha1[5:7])
    mes2= int(pfecha2[5:7])
    dia1= int(pfecha1[8:])
    dia2= int(pfecha2[8:])
    resultAnno= anno2-anno1
    resulMes=(mes2-mes1)
    resulDias=(dia2-dia1)
    if resultAnno == 0:
        if  resulMes<0:
            if resulDias <0:
                return "No es posible calcular la edad, pues no ha podido nacer"
        return "tiene meses no ha cumplido un año"
    elif resultAnno<0:
        return "No es posible calcular la edad, pues no ha podido nacer"
    if resulMes ==0:
            if resulDias<0:
                resultAnno-=1
    elif resulMes<0:
        resultAnno-=1
    return resultAnno




    


#programa principal 
# Reto 3 stringv2
print ("Reto 3 srtingv2")
print(invertirPalabras(input("ingrese una palabra: ")))
print()

# reto 5 stringv2
print("reto 5 stringv2")
print (calcularEdad("1978-11-03", obtenerFecha()))
print (calcularEdad("2000-01-04", obtenerFecha()))
print (calcularEdad("2026-08-26", obtenerFecha()))
print (calcularEdad("2026-01-05", obtenerFecha()))
print()

