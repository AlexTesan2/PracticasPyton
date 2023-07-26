for i in range(5):
    print(i, end=" - ")

frutas=["Sandia","Manzana","Pera","Naraja"]
for i in frutas:
    print(i, end=" ")

for i in range(3,15,3): #pto inicio, pto fin, de cuanto en cuanto
    print(f"Valor de la variable {i}")  #f significa usar funciones especiales


for i in "Zaragoza":
    print("Hola-", end="")  #se realiza el bucle por cada caracter del str

email=False
for i in "correoelecteonico@pruebas.com":
    if i== "@":
        email = True

email=False
correo="correoelecteonico@pruebas.com"
for i in range(len(correo)):
    if correo[i]=="@":
        email = True

if email:
    print("\nEmail correcto")
else: 
    print("\nEmail incorrecto")
