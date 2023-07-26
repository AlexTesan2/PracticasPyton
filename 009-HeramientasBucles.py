for j in "Jaime":
    if j=="m":
        continue    #salta a la siguiente iteración del bucle sin terminar el que se encuentra
    print("letra:   "+j)

nombre="Alex Tesan"
contador=0
print("Caracteres del nombre: "+str(len(nombre)))

for i in nombre:
    if i==" ":
        continue
    contador+=1

print("Numero de letras: "+str(contador))

#while True:
    #pass   #para completarlo luego   ctrl+c

class Miclase:
    pass     # es como si no existiese



email=input("Introduce tu email: ")

for i in email:
    if i=="@":
        arroba=True
        break;
else:               #el else no es del if, sino del for 
    arroba=False
print(arroba)