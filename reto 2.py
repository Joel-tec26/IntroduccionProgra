may=-100000
men= 100000
n=int(input("Escriba la cantidad de números5: "))
i=1
while i<=n:
    num=int(input("Escriba un número: "))
    if num>may:
        may=num
    if num<men:
            men=num
    i=i+1
print("El número mayor es: ", may)
print("El número menor es: ", men)


        