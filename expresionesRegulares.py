#
#
#
#

#importar programas
import re

def validarEdificio (ptexto):
    
    if re.match("^[A-I]{1}\\d{1}\\-{1}\\d{1,2}$", ptexto):
        return True
    else:
        return "Debe especificar un código, vuelva a ingresar el código nuevamente"

def validarcitas (ptexto):

    if re.match("^[C]{1}[A-Z]{1}\\-{1}[0]{1}\\d{1}$", ptexto):
        return "cumple"
    else:
        return "Debe especificar un código, vuelva a ingresar el código nuevamente"

print (validarcitas("CP-01"))