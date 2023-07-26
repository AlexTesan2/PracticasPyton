lista = ["Uno",2,"Tres",4.5,"Cinco"]    #Como vectores, pero se pueden añadir nuevos elemementos

print(lista)
print(lista[2])
print(lista[-2])
print(lista[1:4])   #print(lista[:4]) / print(lista[2:]) no indicar el numero implica principio o final

lista[3] = "Ultimo"
print(lista)
lista.insert(1,"Infiltrado")
print(lista)
print("Infiltrado" in lista)
print(lista.index("Infiltrado"))
print(len(lista))

lista.remove("Ultimo")
print(lista)

lista.pop()     #elimina el ultimo elemento de la lista
print(lista)


lista.append("Manuela")       #introduce nuevo elemento en la ultima posicion
lista.extend(["once","doce"]) #introduce nuevos elementos en la ultima posicion
print(lista)

lista.clear() # borra todos los elementos
print(lista)