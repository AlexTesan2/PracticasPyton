import math
i=0
while i<=10:
    print("Exec "+ str(i), end="- ")
    i=i+1

def edadDelusuario():
    print("\n")
    def preguntarEdad():
        edas=int(input("Introduzca su edad:  "))
        return edas
    
    edad=preguntarEdad()

    while edad!=0:
        print("Su edad es "+str(edad))
        edad=preguntarEdad()
    
    if edad==0:
        print("Felicidades, lograste salir del juego")

edadDelusuario()


def raiz():
    num = int ( input("Introduce un numero para hayar su raiz__"))
    intentos=0

    while num<=0:

        intentos=intentos+1
        print("No se admiten numeros menores de uno("+str(intentos)+str(")__"))
        if intentos>2:
            print("Has gastado tus intentos")
            break

        num = int ( input("Introduce un numero para hayar su raiz__"))

    if intentos<=2:
        print("La raiz de "+str(num)+" es "+ str(math.sqrt(num)))
raiz()