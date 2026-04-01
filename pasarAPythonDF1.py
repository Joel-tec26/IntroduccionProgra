#Joel Jesús Porras Muñoz
#Fecha de creación: 06/03/2026
#Fecha de última modificación: 06/03/2026
#version: 3.14.3

ventaMed=0
ventaPeq=0
ventaGra=0

numeroVent=int(input("Escriba la cantidad de ventas: "))
i=1
while i<=numeroVent:
    costVent=float(input("Escriba el costo de la venta en dolares: "))
    if costVent<=200: 
        ventaPeq=ventaPeq+1
    else:
        if costVent<400:
            ventaMed=ventaMed+1
        else:
            ventaGra=ventaGra+1
    i=i+1
print("La cantidad de ventas pequeñas es: ", ventaPeq)
print("La cantidad de ventas medianas es: ", ventaMed)
print("La cantidad de ventas grandes es: ", ventaGra)
