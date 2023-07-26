#Funcion    Devuelve la lista completa
def pares(limite):
    num=1
    miLista=[]
    while num<limite:
        miLista.append(num*2)
        num+=1
    return miLista

print(pares(10))

print("_______________________________________")

#Generador      Devuelve un unico valor de la lista cada vez que se le llama
def genpares(limite):
    num=1
    while num<limite:
        yield num*2
        num+=1

numPares=genpares(10)

print(next(numPares))   #No se generan los siguientes numeros, ni se les reserva espacio en memoria hasta las siguientes lineas
print("---")
print(next(numPares))
print("---")
print(next(numPares))
print("---")
print(next(numPares))


#for i in numPares:
    #print(i)


def devuele_ciudades(*ciudades):    # * significa: recibira un num indeterminado de elementos en tupla
    for elemento in ciudades:
        yield elemento

cuidades_devueltas=devuele_ciudades("Madrid","Barcelona","Zaragoza","Valencia")
print(next(cuidades_devueltas))
print(next(cuidades_devueltas))
print(next(cuidades_devueltas))
print("________")


def devuele_ciudades1(*ciudades):    #2 recorre los subelementos(caracteres) de los elementos
    for elemento in ciudades:
        for subelemento in elemento:
            yield subelemento

cuidades_devueltas1=devuele_ciudades1("Madrid","Barcelona","Zaragoza","Valencia")
print(next(cuidades_devueltas1))
print(next(cuidades_devueltas1))
print(next(cuidades_devueltas1))
print("________")



def devuele_ciudades2(*ciudades):    # 3 la forma simplificada del anterior
    for elemento in ciudades:
        yield from elemento

cuidades_devueltas2=devuele_ciudades2("Madrid","Barcelona","Zaragoza","Valencia")
print(next(cuidades_devueltas2))
print(next(cuidades_devueltas2))
print(next(cuidades_devueltas2))
print("________")