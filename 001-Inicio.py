
print("Primera linea")  #control + s  para guardar 
texto = "Frasecita"     # shift + alt + flecha abajo para duplicar la linea
print(texto)
print(texto.upper())  # pasa todo a mayusculas
print(texto.lower())  # pasa todo a minusculas
print(texto.find("ci"))  # indica en que posicion se encueltra el valor dado
print(texto.replace("secita","mbuesa"))  

texto2 = texto.replace("ecita","aza").upper()
print(texto2)

print("Frase" in texto) # devuelve boleano indicando si el valor dado se encuentra dento de la variable
print("frase" in texto) 

print (5 ** 3)  # elevevado a 
print(45 > 12)
print(7//2) # división entera

edad = input ("Ingresa tu edad: ")
print(edad)
print(type(edad))  # indica el tipo de dato que es la variable, por defecto será string con los imput

numeroEdad = int(edad)
print(type(numeroEdad))
print(numeroEdad -18)

str(45)
float(45.78)

confirmacion = bool(False)  # siempre será True a menos que le pases:  0, False, None, un str vacio "" 
print(confirmacion)

print(".....................................................")
num = 30                        # operadores logicos, en Java && ||
print (num > 10 and num < 45)
print (num > 10 or num < 45)
print(not(num<18))

if num > 100 :
    print('Es mayor de 100')
elif num >= 50 :
    print ("es mayor de 50")
else :
    print("es pequeño")

lista = ["Uno","Dos","Tres","Cuatro","Cinco"]
print(lista)
print(lista[2])
lista[4] = "Ultimo"
print(lista)
print(lista[-2])
print(lista[1:4])   #print(lista[:4]) / print(lista[2:]) no indicar el numero implica principio o final
lista.insert(1,"Infiltrado")
print(lista)
lista.remove("Cuatro")
print(lista)
print("Infiltrado" in lista)
lista.append("Manuela") #introduce nuevo elemento en la ultima posicion
lista.extend(["once","doce"])
print(len(lista))
lista.clear() # borra todos los elementos
print(lista)

i = 1
while i <= 3:
    print(i)
    i = i + 1

lista = ["Uno","Dos","Tres","Cuatro","Cinco"]

for indice in lista:
    print(indice)

carritoCompra = {   # mapa, diccionario (clave, valor)
    1 : 'Manzana',
    2 : 'Pera',
    3 :'Sandia',
    4 : 'Embutido'
}

print(carritoCompra[3])

tiempo = "soleado"

match tiempo:
    case "lluvia":
        print("Llueve")
    case "soleado":
        print("Hace sol")
    case "terremoto":
        print("Se hizo un terremoto!")
    case _:
        print("Ni idea de cual es el tiempo de hoy")
    

def sumar (num1, num2):     #función 
    return num1+num2

suma= sumar(3,4)            #no se puede llamar a una función antes de que aparezca en el codigo la función
print(suma)

tresSaltos = """Esto es
un texto con 
tres saltos de línea."""
print(tresSaltos)


lista = ["Uno","Dos","Tres","Cuatro","Cinco"]
lista.append("Manuela") #introduce nuevo elemento en la ultima posicion
lista.extend(["once","doce"])
print(lista)
print(lista.index("Cuatro"))
lista.pop() #elimina el ultimo elemento de la lista
print(lista)