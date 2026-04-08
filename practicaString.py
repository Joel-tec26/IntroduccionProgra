#
#
#
#

# funciones
# Reto 4
def eliminarValores (ptexto):
    resultado=""
    biblioteca = "aáAeéEiíIoóOUuúü"
    indice=0
    while indice < len(ptexto):
        letra = ptexto[indice]
        if letra not in biblioteca:
            resultado+=letra
        indice+=1
    return resultado

#Programa Principal
print(eliminarValores("Hola mundo feliz"))
print(eliminarValores("Aarón es niño grande"))
print(eliminarValores("Ana llora por su murciélago"))
print(eliminarValores("Yigüirro de mis amores"))


# funciones
# Reto 4

def esPalindrome (ptexto):
    resultado=""
    indice =-1
    if ptexto =="":
        return "Debe Ingresar un valor para poder ser analizado"
    if len(ptexto)<=3:
        return "La palabra debe tener al menos 3 letras"
    while indice >= -len(ptexto):
        letra= ptexto[indice]
        resultado+= letra
        indice-=1
    return resultado == ptexto

# progarma principal reto 4
print(esPalindrome("salas"))
print(esPalindrome("reconocer"))
print(esPalindrome("pacífico"))
print(esPalindrome(""))
print(esPalindrome("la"))
