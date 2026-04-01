# Creado por: Joel Jesús Porras Muñoz
# Fecha de creación: 11/3/2026 17:25pm
# Ultima modificación: 11/3/2026 18:00pm
# Versión 3.14.3

# Programa Principal

num1 = float(input("Ingrese el número 1: ")) #A
num2 = float(input("Ingrese el número 2: ")) #B
num3 = float(input("Ingrese el número 3: ")) #C

if num1>num2:
    if num1>num3:
        print("El numero: "+str(num1)+ " es el mayor")
    else:
        if num1==num3:
            print("Los números: "+str(num1)+" y "+str(num3)+ " son los mayores")
        else:
            print("El número: "+str(num3)+" es el mayor")
else: 
    if num1==num2:
        if num1>num3:
            print("Los números: "+str(num1)+" y "+str(num2)+ " son los mayores")
        else:
            if num1==num3:
                print("Los números: "+str(num1)+", "+str(num2)+" y "+str(num3)+" son iguales")
            else:
                print("El número: "+str(num3)+" es el mayor")
    else:
        if num2>num3:
            print("El número: "+str(num2)+" es el mayor")
        else:
            if num2==num3:
                 print("Los números: "+str(num2)+" y "+str(num3)+ " son los mayores")
            else:
                print("El número: "+str(num3))


