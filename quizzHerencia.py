# Creado por: Joel Porras, Maria José Espinoza y Alexis Torres
# Fecha de creación: 20/05/2026 9:30am
# Ultima Modificación: 21/05/2026 14:55pm
# Versión: 3.14

# definicion de clase

class Animal:
    def __init__(self, pid, pnombre, ptipo):
        self.idA= pid05
        self.nombreA= pnombre
        self.tipo= ptipo
        return
    
    def mostrarTodo(self):
        print (self.idA)
        print (self.nombreA)
        return 
    
class Mamifero(Animal):
    def __init__(self, pid, pnombre, pduraGest, ptipoGes):
        self.gestacion=(pduraGest, ptipoGes)
        Animal.__init__(self, pid,pnombre,"Mamífero")
        return
    def mostrar(self):
        Animal.mostrarTodo(self)
        print(self.gestacion[0], tipo(self.gestacion))

class Ave(Animal):
    def __init__(self, pid, pnombre, paltura):
        self.alturaMaxima=paltura
        Animal.__init__(self, pid,pnombre,"Ave")
        return
    def mostrar(self):
        Animal.mostrarTodo(self)
        print(self.alturaMaxima)

#definicion de funciones

def tipo (ptipo):
    if ptipo[1]==1:
        return "Semanas"
    elif ptipo[1]== 2:
        return "Meses"

# menú

listaDeAnimales=[]

while True:
    print ("---Registro de Animales---")
    print ("1 - Agregue Mamífero")
    print ("2 - Agregue Ave")
    print ("3 - Ver Mamífero")
    print ("4 - Ver Ave")          
    print ("5 - Salir")
    opcion= input("Digite su opción: ")
    if opcion=="1":
        print ("***Indique los datos del Mamífero***")
        id = input("Id: ")
        nombre = input("Nombre: ")
        duracionGestacion = int(input("duracion de gestación: "))
        tipoGes= int(input("tipo de gestación (1: semanas, 2: Meses): "))
        nuevomaf=Mamifero(id, nombre, duracionGestacion, tipoGes)
        listaDeAnimales.append(nuevomaf)
    elif opcion=="2":
        print ("***Indique los datos del Ave***")
        id = input("Id: ")
        nombre = input("Nombre: ")
        alturaMax= int(input("Altura Maxima: "))
        nuevAve=Ave(id, nombre, alturaMax)
        listaDeAnimales.append(nuevAve)
    elif opcion == "3":
         print ("***Indique el valor de búsqueda para obtener los datos del Mamífero***")
         id= input("id: ")
         for animal in listaDeAnimales:
            if animal.tipo == "Mamífero":
               if animal.idA == id:
                  animal.mostrar()
    elif opcion == "4":
         print ("***Indique el valor de búsqueda para obtener los datos del Ave***")
         id= input("id: ")
         for animal in listaDeAnimales:
            if animal.tipo == "Ave":
               if animal.idA == id:
                  animal.mostrar()
    else:
        print("Opción incorrecta")

    





        


    