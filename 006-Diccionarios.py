diccionario = {"España":"Madrid", "Francia":"Paris", "Italia":"Roma", "Portugal":"Lisboa"}

print(diccionario["Italia"])      #Muestra el valor asociado a la clave Italia

diccionario["Alemania"]="Belanga" #Agregar new elementos
diccionario["Alemania"]="Belin"   #No puede haber dos claves = en el mismo diccionario el valor se sobreescribe 

del diccionario["Francia"]        #Eliminar
print(diccionario);

print(diccionario.keys())
print(diccionario.values())
print(len(diccionario))

print("\n")
diccionario2={2:"Lechuga", "Alimentacion":4, 9:7.3 , "Mx":"Mexico"} #Acepta toda clase de valores
tupla=["España","Francia", "Italia"]
diccionario3={tupla[0]:"Madrid", tupla[1]:"Paris", tupla[2]:"Roma"}
print(diccionario3)
diccionario4={"Clase":"A", 1:True, "Fechas":[2015,2016,2017,2018]}  #Tupla dentro de un diccionario
print(diccionario4["Fechas"])
diccionario5={"Clase":"C","Cursos":{1:True,2:False,3:False,4:True,"Fechas":[2015,2016]}}#dicc dentro de dicc con tupla
print(diccionario5["Cursos"])

carritoCompra = {
    1 : 'Manzana',
    2 : 'Pera',
    3 :'Sandia',
    4 : 'Embutido'
}
print(carritoCompra[3])