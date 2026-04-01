#Joel Jesús Porras Muñoz
#Fecha de creación: 06/03/2026 11:25am
#Fecha de última modificación: 06/03/2026 11:45am
#version: 3.14.3

llamadaL=0
cuenta=0.0
tipoCarac= input("Escriba el tipo de llamada (I para internacional, L para local y N para nacional): ")
duracion=int(input("Escriba la duración de la llamada en minutos: "))
while tipoCarac!="x" and duracion!=-1:
    if tipoCarac=="I":
        if duracion> 3:
            costo = 7.59+(duracion-3)*3.03
        else:
            costo=7.59
    elif tipoCarac=="L":
        cuenta=cuenta+1
        if cuenta> 50:
            costo=0.60
        else:
            costo=0
    elif tipoCarac=="N":
        if duracion>3:
            costo = 1.20+(duracion-3)*0.48
        else:
            costo=1.20
    cuenta=cuenta+costo
    tipoCarac= input("Escriba el tipo de llamada (I para internacional, L para local y N para nacional): ")
    duracion=int(input("Escriba la duración de la llamada en minutos: "))
print("El costo total de las llamadas es: ", cuenta)
