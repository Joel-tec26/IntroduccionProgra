# Creado por: Joel Jesús Porras Muñoz, Alexis Torres y crsitopher Jara
# Fecha de creación: 29/04/2026 9:30am
# Ultíma modificación: 29/4/2026 10am
# Versión: 3.14

#  definicion de funciones

# reto 1
def infectarVirus(pmatriz, pnum):
    fila = 0
    while fila < len(pmatriz):
        columna = 0
        while columna <len(pmatriz[fila]):
            if columna==pnum:
                pmatriz [fila][columna]= "error"
            if pnum>len(pmatriz[fila]):
                pmatriz [fila][-1]= "error"
            columna+=1
        fila+=1
    return print (pmatriz)

# reto 3
def buscarEnMatriz(pmatriz, pnum):
    fila = 0
    contador1 = 0
    while fila < len(pmatriz):
        columna = 0
        while columna <len(pmatriz[fila]):
            if pmatriz [fila][columna]==pnum:
                print (str(fila)+","+str(columna))
                contador1+= 1
            columna+=1
        fila+=1
    if contador1==0:
        print ("-1,-1")
    return

def definirPiramide(pmatriz):
    linea1= pmatriz[0]
    lineaFinal=pmatriz[-1]
    resultado= (linea1[0])+(linea1[-1])+(lineaFinal[0])+(lineaFinal[-1])
    print(f"El número pirámide es: {resultado}")
    return

def esCuadrada(pmatriz):
    filas=len(pmatriz)
    for i in pmatriz:
        if len(i)!=filas:
            return False
    return True
def imprimirEquis(pmatriz):
    equis=""
    numMasGrasde=0
    tamannoMatriz=len(pmatriz)
    if not esCuadrada(pmatriz):
        print("la matriz debe ser cuadrada")
    for i in range(tamannoMatriz):
        equis+=str(pmatriz[i][i])+","
        if pmatriz[i][i]>numMasGrasde:
            numMasGrasde=pmatriz[i][i]
        pmatriz[i][i]="a"
    for i in range(1,tamannoMatriz+1):
        if isinstance(pmatriz[i-1][-i], int):
            equis+=str(pmatriz[i-1][-i])+","
            if pmatriz[i-1][-i]>numMasGrasde:
                numMasGrasde=pmatriz[i][i]
    print(f"los valores de la X son: {equis}")
    print(f"el valor mas grande es: {numMasGrasde}")

def analizarMatriz(notas):
    if notas==[]:
        print("Matriz vacia")
    for i in notas:
        if len(i)!=8:
            print("la matriz debe tener 8 columnas")
            return
    for i in notas:
        notaAlta=0
        notaBaja=100
        promedio=0
        divicion=0
        for o in i:
            if o>notaAlta:
                notaAlta=o
            if o<notaBaja:
                notaBaja=o
            promedio+=o
            divicion+=1
        promedio/=divicion
        if promedio>=70:
            condicion="Áprobado"
        else:
            condicion="Réprobado"
        print([notaAlta,notaBaja,round(promedio,2),condicion])
    return
    
def esDeclinada(pmatriz):
    columnas=len(pmatriz[0])
    for i in pmatriz:
        if len(i)!=columnas:
            return "el dato ingresado no corresponde a una matriz"
    for i in pmatriz:
        mayor=max(i)+1
        for o in i:
            if o<mayor:
                mayor=o
            else:
                return False
    return True
            

def esPrimo(pnum):
    if pnum!=1:
        for i in range(2,pnum):
            if pnum%i==0:
                return False
    else:
        return False
    return True

def extraerPrimos(pmatriz, pfila, pcolumna):
    primos=[]
    tamannoColumna=len(pmatriz[0])
    if not isinstance(pmatriz, list):
        print("Todos los elementos de la matriz deben ser listas.")
        return
    for i in pmatriz:
        if len(i)!=tamannoColumna:
            print("El valor de entrada no es una matriz")
            return
        if not isinstance(i, list):
            print("Todos los elementos de la matriz deben ser listas.")
            return
    if not isinstance(pfila, int) or not isinstance(pcolumna, int):
        print("Los datos para la fila y la columna deben ser enteros únicamente.")
        return
    if pfila>len(pmatriz):
        print("El número de fila solicitado excede la cantidad de filas de la matriz ingresada.")
        return
    if pcolumna>tamannoColumna:
        print("El número de columna solicitada excede la cantidad de columnas de la matriz ingresada.")
        return
    pfila-=1
    pcolumna-=1
    try:
        for i in range(pfila, len(pmatriz)):
            try:
                for o in range(pcolumna, tamannoColumna):
                    numero=pmatriz[i][o]
                    if esPrimo(numero):
                        if numero not in primos:
                            primos.append(numero)
            except IndexError:
                print("El número de columna solicitada excede la cantidad de columnas de la matriz ingresada.")
                return
    except IndexError:
        print("El número de fila solicitado excede la cantidad de filas de la matriz ingresada. ")
        return
    print(primos)
    return

# programa principal
print("reto 1")
print("Entrada: \ninfectarVirus([[10, 11, 30 ], [25, 10, 15]], 1)")
print("Salida:")
infectarVirus([[10, 11, 30 ], [25, 10, 15]], 1)
print("Entrada: \ninfectarVirus ([[10, 11, 30 ], [25, 10, 15]], 9)")
print("Salida: ")
infectarVirus ([[10, 11, 30 ], [25, 10, 15]], 9)
print()
print("reto 3")
print("Entrada: \nbuscarEnMatriz([[1,2],[3,4]],1)")
print("Salida:")
buscarEnMatriz([[1,2],[3,4]],1)
print("Entrada: \nbuscarEnMatriz([[1,2,3],[4,5,6]],7) ")
print("Salida:")
buscarEnMatriz([[1,2,3],[4,5,6]],7) 
print("Entrada: \nbuscarEnMatriz ([[1,2,3],[4,5,6],[7,8,9]],8)")
print("Salida:")
buscarEnMatriz ([[1,2,3],[4,5,6],[7,8,9]],8)
print()
print("reto 5")
print("Entrada: \ndefinirPiramide([[1,2,3],[4,5,6],[7,8,9]])")
print("Salida:")
definirPiramide([[1,2,3],[4,5,6],[7,8,9]])
print("Entrada: \ndefinirPiramide([[13,12,23,14],[17,25,16,15],[11,18,19,21]])")
print("Salida:")
definirPiramide([[13,12,23,14],[17,25,16,15],[11,18,19,21]])
print("reto6") 
imprimirEquis([[10,99,23,34],[34,67,3,12],[7,23,65,78],[45,2,34,7]])
imprimirEquis([[10,99,23,34,40],[34,67,3,12,83],[7,23,65,78,12],[45,2,34,7,15],[1,2,3,4,5]])
print()
print("reto8")
analizarMatriz([])
print()
analizarMatriz([[1,2,3,4,5,6,7]])
print()
notas=[[100,76,82,63,49,51,81,97]]
analizarMatriz(notas)
print()
analizarMatriz([[100,76,82,63,49,51,81,97],[72,66,80,35,77,60,70,71],[80,81,91,59,55,75,56,87],[59,65,78,74,91,81,60,67]])
print()
analizarMatriz([[100,76,82,63,49,51,81,97],[72,66,80,35,77,60,70,71],[67,15,70,52,71,90,60,87],[80,81,91,59,55,75,56,87],[90,11,71,69,75,85,36,57],[59,65,78,74,91,81,60,67]])
print()
print("reto10")
print(esDeclinada([[1,17,23],[31,1,1,11]]))
print(esDeclinada([[1,17,23,1],[31,1,1,11],[89,1,1,53]]))
print(esDeclinada([ [17,10,7],[23,4,1],[120,89,23]]))
print()
print("reto11")
extraerPrimos([[23,20],[25,37,1],[50,24,58],[79,61,14]],2,1)
print()
extraerPrimos([[23,20,17],(25,37,1),[50,24,58],[79,61,14]],2,1)
print()
extraerPrimos([[23,20,17],[25,37,1],[50,24,58],[79,61,14]],"a",1)
print()
extraerPrimos([[23,20,17],[25,37,1],[50,24,58],[79,61,14]],5,1)
print()
extraerPrimos([[23,20,17],[25,37,1],[50,24,58],[79,61,14]],1,5)
print()
extraerPrimos([[23,20,17],[25,37,1],[50,24,58],[79,61,14]],2,1)
print()
extraerPrimos([[15,97],[53,89],[43,10]],1,1)
print()
extraerPrimos([[37,1],[24,58],[61,14]],1,1) 
print()
extraerPrimos([[7,6,12],[55,39,17]],2,2)
print()
extraerPrimos([[50,6],[55,39]],1,1)
print()