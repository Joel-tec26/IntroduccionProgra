# inicio de variables
num1=0
num2=0
ope=0

# entrada de Datos 
print("Digite número 1, número 2")
print("Para las operaciones digite: 1 para suma, 2 para resta, 3 para multiplicación y 4 para divición")
#operacion 
num1= float(input("Número 1:"))
num2= float(input("Número 2:"))
ope= int(input("Operación:"))
if ope==1:
    print("El resultado es " + str(num1+num2))
elif ope==2:
    print("El resultado es "+ str(num1-num2))
elif ope==3:
    print("El resultado es "+ str(num1*num2))
elif ope==4:
    if num2!=0:
        print("El resultado es "+ str(num1/num2))
    else:
        print("Error, no se puede dividir entre 0")
else:
    print("Número NO valido")
