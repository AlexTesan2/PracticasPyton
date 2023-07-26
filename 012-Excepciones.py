def evaluarEdad(edad):
    if edad<0:
        raise TypeError("No pongas edad negativa")
    if edad <20:
        return"Eres muy joven"
    elif edad <40:
        return"Eres joven"
    elif edad <65:
        return"Eres mayorcito"
    elif edad <100:
        return"Eres mayor de 100"

print(evaluarEdad(23))

print("__________")

import math
def raiz(num):
    if num<0:
        raise ValueError("No se aceptan numeros negativos")
    else:
        return math.sqrt(num)

print(raiz(-4))