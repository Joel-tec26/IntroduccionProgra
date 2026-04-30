# Creado por: Joel Jesús Porras Muñoz, Alexis Torres y crsitopher Jara
# Fecha de creación: 29/04/2026 9:30am
# Ultíma modificación: 29/4/2026 10am
# Versión: 3.14

# definicial de funcial 

def validarMatrizCuadrada (pmatriz):
    for i in pmatriz:
        if len(pmatriz) !=  len(i):
            return False
    return True

def obtenerDiagonal (pmatriz):
    if not validarMatrizCuadrada(pmatriz):
        print("La matriz debe ser cuadrada.")
        return
    salida= obtenerDiagonalProcesar(pmatriz)
    print(salida)
    return


def obtenerDiagonalProcesar(pmatriz):
    salida = ""
    for i in range(len(pmatriz)):
        salida += str(pmatriz[i][i])
        if i != len(pmatriz) - 1:
            salida += ","
    return salida


obtenerDiagonal([[5,43,98,25],[78,23,5,54],[23,56,67,87],[56,23,56,45]])
obtenerDiagonal([[5,43,98],[78,23,5,54],[23,56,67,87],[56,23,56,45]])

