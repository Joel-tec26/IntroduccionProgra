masue=0
numeroP=int(input("Escriba la cantidad de empleados: "))
i=1
while i<=numeroP:
    numEmp=int(input("Escriba el número de empleado: "))  
    sueldo=float(input("Escriba el sueldo del empleado: "))
    if sueldo>masue:
        masue=sueldo  
        manum=numEmp
    i=i+1
print("El número de empleado con el sueldo más alto es: ", manum)
print("El sueldo más alto es: ", masue)
    