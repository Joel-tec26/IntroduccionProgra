# Creado por: Joel Jesús Porras Muñoz, Alexis Torres, Christopher Jara y Maria Jose Espinoza
# Fecha de creación: 29/04/2026 9:30am
# Ultíma modificación: 30/4/2026 11am
# Versión: 3.14

#  definicion de funciones

# reto 1
def infectarVirus(pmatriz, pnum):
    """
Funcionamiento: Recorre la matriz y cambia el valor de la columna indicada por "error" en cada fila. 
Si el número de columna no existe, cambia el último elemento.
Entradas:
- pmatriz(list): La matriz que se va a modificar.
- pnum(int): El número de columna que se quiere infectar.
Salidas:
- pmatriz(list): La matriz con los valores reemplazados por "error".
    """
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

#Reto 3
def buscarEnMatriz(pmatriz, pnum):
    """ 
Funcionamiento: Busca un número dentro de la matriz e imprime en qué fila y columna aparece. 
Si no lo encuentra, imprime -1,-1.
Entradas:
- pmatriz(list): La matriz donde se va a buscar.
- pnum(int): El número que se quiere encontrar.
Salidas:
- coordenadas(str): Las posiciones "fila,columna" donde aparece el número, o "-1,-1" si no está.
    """
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

#Reto 5
def definirPiramide(pmatriz):
    """
Funcionamiento: Suma las cuatro esquinas de la matriz y muestra el resultado
junto con el proceso de la suma.
Entradas:
- pmatriz(list): La matriz de la que se sacan las esquinas.
Salidas:
- resultado(int): La suma de las cuatro esquinas de la matriz.
    """
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
    """
Funcionamiento: Extrae los números de las dos diagonales de una matriz cuadrada formando una X
 y determina cuál es el mayor entre todos ellos.
Entradas:
- pmatriz(list): La matriz cuadrada sobre la que se traza la X.
Salidas:
- valores(str): Los números que forman la X separados por comas.
- mayor(int): El número más grande encontrado en la X.
    """
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

#Reto 8
def analizarMatriz(notas):
    """
Funcionamiento: Por cada fila (estudiante) calcula la nota más alta, la más baja y el promedio
y determina si aprobó (promedio >= 70) o reprobó.
Si la matriz está vacía o no tiene 8 columnas, avisa del error.
Entradas:
- notas(list): Matriz donde cada fila tiene exactamente 8 notas numéricas.
Salidas:
- resumen(list): Por cada estudiante imprime [nota alta, nota baja, promedio, condición].
    """
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

 #Reto 10   
def esDeclinada(pmatriz):
    """
Funcionamiento: Revisa que todas las filas tengan el mismo número de columnas y que los valores de cada fila 
vayan de mayor a menor estrictamente.
Entradas:
- pmatriz(list): La matriz que se quiere evaluar.
Salidas:
- resultado(bool/str): True si es declinada, False si no lo es,
o un mensaje de error si las filas no tienen el mismo tamaño.
    """
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
            
#Reto 11
def esPrimo(pnum):

    if pnum!=1:
        for i in range(2,pnum):
            if pnum%i==0:
                return False
    else:
        return False
    return True

def extraerPrimos(pmatriz, pfila, pcolumna):
    """
Funcionamiento: Valida que la entrada sea una matriz rectangular de listas y que los índices existan.
 Desde la posición indicada recorre la matriz buscando números primos sin repetirlos y los devuelve en una lista.
Entradas:
- pmatriz(list): La matriz con los números a revisar.
- pfila(int): Fila desde donde empezar a buscar (contando desde 1).
- pcolumna(int): Columna desde donde empezar a buscar (contando desde 1).
Salidas:
- primos(list): Lista con todos los números primos únicos encontrados,
o mensajes de error según lo que falle en la validación.
    """
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

#Programa principal

#PP reto 1
print("reto 1")
print("Entrada: \ninfectarVirus([[10, 11, 30 ], [25, 10, 15]], 1)")
print("Salida:")
infectarVirus([[10, 11, 30 ], [25, 10, 15]], 1)
print("Entrada: \ninfectarVirus ([[10, 11, 30 ], [25, 10, 15]], 9)")
print("Salida: ")
infectarVirus ([[10, 11, 30 ], [25, 10, 15]], 9)
print()

#PP reto 3
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

#PP reto 5
print("reto 5")
print("Entrada: \ndefinirPiramide([[1,2,3],[4,5,6],[7,8,9]])")
print("Salida:")
definirPiramide([[1,2,3],[4,5,6],[7,8,9]])
print("Entrada: \ndefinirPiramide([[13,12,23,14],[17,25,16,15],[11,18,19,21]])")
print("Salida:")
definirPiramide([[13,12,23,14],[17,25,16,15],[11,18,19,21]])

#PP reto 6
print("reto6") 
print ("Entrada:imprimirEquis([[10,99,23,34],[34,67,3,12],[7,23,65,78],[45,2,34,7]]) ")
print("Salida:")
imprimirEquis([[10,99,23,34],[34,67,3,12],[7,23,65,78],[45,2,34,7]])
print ("Entrada:imprimirEquis([[10,99,23,34,40],[34,67,3,12,83],[7,23,65,78,12],[45,2,34,7,15],[1,2,3,4,5]]")
print("Salida:")
imprimirEquis([[10,99,23,34,40],[34,67,3,12,83],[7,23,65,78,12],[45,2,34,7,15],[1,2,3,4,5]])
print()

#PP reto 8
print("reto8")
print ("Entrada: analizarMatriz([])")
print("Salida:")
analizarMatriz([])
print ("Entrada: analizarMatriz([[1,2,3,4,5,6,7]])")
print("Salida:")
analizarMatriz([[1,2,3,4,5,6,7]])
print ("Entrada: notas=[[100,76,82,63,49,51,81,97]] analizarMatriz(notas)")
print("Salida:")
notas=[[100,76,82,63,49,51,81,97]]
analizarMatriz(notas)
print ("Entrada: analizarMatriz([[100,76,82,63,49,51,81,97],[72,66,80,35,77,60,70,71],[80,81,91,59,55,75,56,87],[59,65,78,74,91,81,60,67]])")
print("Salida:")
analizarMatriz([[100,76,82,63,49,51,81,97],[72,66,80,35,77,60,70,71],[80,81,91,59,55,75,56,87],[59,65,78,74,91,81,60,67]])
print ("Entrada: analizarMatriz([[100,76,82,63,49,51,81,97],[72,66,80,35,77,60,70,71],[67,15,70,52,71,90,60,87],[80,81,91,59,55,75,56,87],[90,11,71,69,75,85,36,57],[59,65,78,74,91,81,60,67]])")
print("Salida:")
analizarMatriz([[100,76,82,63,49,51,81,97],[72,66,80,35,77,60,70,71],[67,15,70,52,71,90,60,87],[80,81,91,59,55,75,56,87],[90,11,71,69,75,85,36,57],[59,65,78,74,91,81,60,67]])
print()

#PP reto 10
print("reto10")
print("Entrada: print(esDeclinada([[1,17,23],[31,1,1,11]]))")
print("Salida:")
print(esDeclinada([[1,17,23],[31,1,1,11]]))
print("Entrada:print(esDeclinada([[1,17,23,1],[31,1,1,11],[89,1,1,53]]))")
print("Salida:")
print(esDeclinada([[1,17,23,1],[31,1,1,11],[89,1,1,53]]))
print("Entrada: print(esDeclinada([ [17,10,7],[23,4,1],[120,89,23]]))")
print("Salida:")
print(esDeclinada([ [17,10,7],[23,4,1],[120,89,23]]))
print()

#PP reto 11
print("reto11")
print("Entrada: extraerPrimos([[23,20],[25,37,1],[50,24,58],[79,61,14]],2,1)")
print("Salida:")
print("Entrada:extraerPrimos([[23,20],[25,37,1],[50,24,58],[79,61,14]],2,1) ")
extraerPrimos([[23,20],[25,37,1],[50,24,58],[79,61,14]],2,1)
print("Salida:")
extraerPrimos([[23,20,17],(25,37,1),[50,24,58],[79,61,14]],2,1)
print('Entrada: extraerPrimos([[23,20,17],[25,37,1],[50,24,58],[79,61,14]],"a",1)')
print("Salida:")
extraerPrimos([[23,20,17],[25,37,1],[50,24,58],[79,61,14]],"a",1)
print("Entrada: extraerPrimos([[23,20,17],[25,37,1],[50,24,58],[79,61,14]],5,1)")
print("Salida:")
extraerPrimos([[23,20,17],[25,37,1],[50,24,58],[79,61,14]],5,1)
print("Entrada: extraerPrimos([[23,20,17],[25,37,1],[50,24,58],[79,61,14]],1,5)")
print("Salida:")
extraerPrimos([[23,20,17],[25,37,1],[50,24,58],[79,61,14]],1,5)
print("Entrada: extraerPrimos([[23,20,17],[25,37,1],[50,24,58],[79,61,14]],2,1)")
print("Salida:")
extraerPrimos([[23,20,17],[25,37,1],[50,24,58],[79,61,14]],2,1)
print("Entrada: extraerPrimos([[15,97],[53,89],[43,10]],1,1)")
print("Salida:")
extraerPrimos([[15,97],[53,89],[43,10]],1,1)
print("Entrada: extraerPrimos([[37,1],[24,58],[61,14]],1,1) ")
print("Salida:")
extraerPrimos([[37,1],[24,58],[61,14]],1,1) 
print("Entrada: extraerPrimos([[7,6,12],[55,39,17]],2,2)")
print("Salida:")
extraerPrimos([[7,6,12],[55,39,17]],2,2)
print("Entrada: extraerPrimos([[50,6],[55,39]],1,1)")
print("Salida:")
extraerPrimos([[50,6],[55,39]],1,1)