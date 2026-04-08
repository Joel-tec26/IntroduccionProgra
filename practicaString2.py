# Creado por: Joel Porras, Maria José Espinoza y Alexis Torres
# Fecha de creación: 8/4/2026 8:30am
# Ultima Modificación: 8/4/2026 14:10pm
# Versión: 3.14

# definicion de funciones
# Reto 3 stringv2
def invertirPalabras (ptexto):
    """
    Funcionalidad:
    Invierte el texto ingresado siempre que termine en una vocal. Luego solicita
    nuevamente una palabra al usuario de forma recursiva.
    Entradas:
    -ptexto(str): texto o palabra ingresada por el usuario que se desea invertir
    Salidas:
    -resultado(str): texto invertido 
    """
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
    """
    Funcionalidad:
    Obtiene la fecha actual del sistema.
    Entradas:
    -No tiene entradas
    Salidas:
    -hoy(str): fecha actual en formato aaaa-mm-dd
    """
    hoy=date.today()
    return str(hoy)

def calcularEdad (pfecha1, pfecha2):
    """
    Funcionalidad:
    Calcula la edad en años a partir de dos fechas (fecha de nacimiento y fecha actual),
    validando si la persona aún no ha nacido o si no ha cumplido un año.
    Entradas:
    -pfecha1(str): fecha inicial  en formato aaaa-mm-dd
    -pfecha2(str): fecha final en formato aaaa-mm-dd
    Salidas:
    -resultAnno(int/str): edad en años o mensaje indicando error o condición especial
    """
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


# reto 3 paracticaParte2

def despedasarUrl (ptexto):
    """
    Funcionalidad:
    Analiza una URL para identificar el protocolo, el tipo de protocolo,
    el nombre del host y el tipo de recurso solicitado.
    Entradas:
    -ptexto(str): URL que se desea analizar
    Salidas:
    -resultado(str): descripción del protocolo, host y recurso de la URL
    """
    if "https://" in ptexto:
        nomProt="HTTPS"
        tipoProt= "Seguro"
    elif "http://" in ptexto:
        nomProt="HTTP"
        tipoProt= "Estándar"
    elif "ftp://" in ptexto:
        nomProt="FTP"
        tipoProt= "Simple"
    bandera1=True
    bandera2=True
    for i in range(len(ptexto)):
        if bandera1:
            if ptexto[i] == "w":
                inicio= i
                bandera1=False
        if not bandera1:
            if bandera2:
                if ptexto[i] == "/":
                    fin= i
                    bandera2=False
    nomHost= ptexto[inicio:fin]
    if "index" in ptexto or "default" in ptexto:
        recurso="Página inicial"
    else:
        recurso= "cualquier otra pagina del sitio web"
    tipoRecurso= ptexto[-3:]
    return f"Nombre del Protocolo: {nomProt} \n Por ende es un protocolo: {tipoProt} \n Nombre del Host: {nomHost} \n Recurso: {recurso} \n Concideración del recurso: {tipoRecurso}"



#programa principal 
# Reto 3 stringv2
print ("Reto 3 srtingv2")
print(invertirPalabras(input("ingrese una palabra: ")))
print()

# reto 5 stringv2
print("\n reto 5 stringv2")
print (calcularEdad("1978-11-03", obtenerFecha()))
print (calcularEdad("2000-01-04", obtenerFecha()))
print (calcularEdad("2026-08-26", obtenerFecha()))
print (calcularEdad("2026-01-05", obtenerFecha()))
print()

# reto 3 examenParte2
print("\n reto 3 examenParte2")
print(despedasarUrl("http://www.alegsa.com.ar/Diccionario/index.php"))

