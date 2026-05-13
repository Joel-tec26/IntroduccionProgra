# Creado por: Joel Porras, María José Espinoza y Alexis Torres
# Fecha de creación: 06/05/2026 10am
# Ultima modificación: 13/05/2026 3pm
# versión: 3.14

#definicion de clases

class platillo:
    """
    Funcionalidad:
    Representa un platillo con información de identificación,
    nombre, ingredientes y precio.
    """

    def __init__(self):
        """
        Funcionalidad:
        Inicializa los atributos del objeto platillo con valores por defecto.

        Entradas:
        -No tiene entradas

        Salidas:
        -id(str): identificador inicial vacío
        -nombre(str): nombre inicial vacío
        -ingrediente(list): lista inicial vacía de ingredientes
        -precio(int/float): precio inicial en 0
        """
        self.id=""
        self.nombre=""
        self.ingrediente=[]
        self.precio=0
        return

    def asignarId(self, id):
        """
        Funcionalidad:
        Asigna un identificador al platillo.
        Entradas:
        -id(str): identificador del platillo
        Salidas:
        -No retorna valores (modifica el atributo id)
        """
        self.id=id
        return
        
    def asignarNombre(self, nombre):
        """
        Funcionalidad:
        Asigna un nombre al platillo.
        Entradas:
        -nombre(str): nombre del platillo
        Salidas:
        -No retorna valores (modifica el atributo nombre)
        """
        self.nombre=nombre
        return

    def asignarIngrediente(self, ingrediente):
        """
        Funcionalidad:
        Asigna la lista de ingredientes del platillo.
        Entradas:
        -ingrediente(list): lista de ingredientes del platillo
        Salidas:
        -No retorna valores (modifica el atributo ingrediente)
        """
        self.ingrediente=ingrediente
        return

    def asignarPrecio(self, precio):
        """
        Funcionalidad:
        Asigna el precio del platillo.
        Entradas:
        -precio(int/float): precio del platillo
        Salidas:
        -No retorna valores (modifica el atributo precio)
        """
        self.precio=precio
        return

    def obtenerId(self):
        """
        Funcionalidad:
        Obtiene el identificador del platillo.
        Entradas:
        -No tiene entradas
        Salidas:
        -id(str): identificador del platillo
        """
        return self.id
    
    def obtenerNombre(self):
        """
        Funcionalidad:
        Obtiene el nombre del platillo.
        Entradas:
        -No tiene entradas
        Salidas:
        -nombre(str): nombre del platillo
        """
        return self.nombre
    
    def obtenerIngrediente(self):
        """
        Funcionalidad:
        Obtiene la lista de ingredientes del platillo.
        Entradas:
        -No tiene entradas
        Salidas:
        -ingrediente(list): lista de ingredientes del platillo
        """
        return self.ingrediente
    
    def obtenerPrecio(self):
        """
        Funcionalidad:
        Obtiene el precio del platillo.
        Entradas:
        -No tiene entradas
        Salidas:
        -precio(int/float): precio del platillo
        """
        return self.precio
    
    def mostrarTodo(self):
        """
        Funcionalidad:
        Retorna toda la información almacenada del platillo.
        Entradas:
        -No tiene entradas
        Salidas:
        -id(str): identificador del platillo
        -nombre(str): nombre del platillo
        -ingrediente(list): lista de ingredientes
        -precio(int/float): precio del platillo
        """
        return self.id, self.nombre, self.ingrediente, self.precio
    
#programa principal

plato1=platillo()

vid=input("ingrese el codigo del platillo: ")
plato1.asignarId(vid)
vnombre=input("ingrese el nombre del platillo: ")
plato1.asignarNombre(vnombre)

ingredientes=[]
while True:
    seleccion=input("Desea ingresar un ingrediente? (1:si 2:no): ")
    if seleccion=="1":
        ingrediente=input("ingrese el ingrediente que desea: ")
        ingredientes.append(ingrediente)
    elif seleccion=="2":
        print("Continuando.")
        break
    else:
        input("opcion inválida.\nprecione ENTER para continuar")
plato1.asignarIngrediente(ingredientes)

vprecio=input("ingrese el precio del platillo: ")
plato1.asignarPrecio(vprecio)

print(f"Id del platillo: {plato1.obtenerId()}")
print(f"nombre del platillo: {plato1.obtenerNombre()}")
for i in range(len(plato1.obtenerIngrediente())):
    print(f"ingrediente #{i+1}: {plato1.obtenerIngrediente()[i]}")
print(f"precio del platillo: {plato1.obtenerPrecio()}")