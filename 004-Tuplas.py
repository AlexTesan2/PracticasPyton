tupla = ("Juan","Ana","Manuel","Enrique","Susana","German","Nayra","Manuel") 

#listas [], tuplas ()   Su finalidad es ser consultadas
#el contenido de las tuplas no se pueden modificar, no aceptan .append, .pop, .extend ...

print(tupla[5])
lista=list(tupla)
tupla2=tuple(lista)
print(tupla)
print(lista)

print("Juan" in tupla)
print(tupla.count("Manuel"))
print(len(tupla))

tupla3=9,"julio",2023, "Alex"
dia,mes,anyo,nombre = tupla3;
print(nombre, dia, mes, anyo)

tupla4 = tupla + tupla3
print(tupla4)