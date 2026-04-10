# creado por: Joel Porras, Maria José Espinoza, Cristopher Jara y Alexis Torre
# Fecha de creacion: 10/04/2026 10am
# Ultima actualizacion: 10/04/2026 10am
# Version: 3.14

#definir funciones
def encontrarAlMenos0(plista):
    """
    funcionamiento: dice si una lista contiene al menos un 0
    entradas:
    -plista(lista): lista de numeros ingresada por el usuario
    salida: True/False
    """
    for i in plista:
        if i==0:
            return True
    return False

def contarRepeticionesL(plista, pdigito):
    contador=0
    for i in plista:
        if i==pdigito:
            contador+=1
    if contador==0:
        return "No se encuentra"
    return contador

def acumularSuma(plista):
    num=0
    lista2=[]
    for i in plista:
        num+=i
        lista2.append(num)
    return lista2

def eliminarDuplicado(plista):
    nuevaLista=[]
    for i in plista:
        if i not in nuevaLista:
            nuevaLista.append(i)
    return nuevaLista

def eliminarEspacios(ptexto):
    nuevoTexto=""
    contador =0
    for i in ptexto:
        if i!=" ":
            nuevoTexto+=i
        else:
            contador+=1
    return [[nuevoTexto],[contador]]

#programa principal

print("ejercicio 4")
print(encontrarAlMenos0([8,0,6,5,0,3]))
print(encontrarAlMenos0([8,5,6,5,3]))
print()
print("reto6")
print(contarRepeticionesL([8,0,6,5,0,3],4))
print(contarRepeticionesL([8,2,6,8,4],8))
print(contarRepeticionesL([2,3,4,5,7],5))
print()
print("reto10")
print(acumularSuma([1,2,3]))
print(acumularSuma([1,4,8,2]))
print()
print("reto14")
print(eliminarDuplicado([1,2,3,2,5]))
print(eliminarDuplicado(["a","b","c"]))
print(eliminarDuplicado([1,2,3,2,5,3,4,3]))
print()
print("reto18")
print(eliminarEspacios("Hoy es un buen día para ser feliz."))