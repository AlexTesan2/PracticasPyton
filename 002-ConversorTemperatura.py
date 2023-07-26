#Este ejercicio recibirá un numero de grados y una letra que indicará la escala
#Hay que pasar los Celsius a kelvin y viceversa

temperatura = float(input("Ingrese la tempreatura en grados "))
escala= input("Ingrese la escala Celsius (C) o Kelvin (K) ").upper()

if escala in ("C","K"):
    print("cargando...")
    if escala == "C" :
        print("La temperatura es ",(temperatura + 273), " grados Kelvin")
    elif escala == "K" :
        print("La temperatura es ",(temperatura - 273), " grados Centigrados")
else :
    print("Escala incorrecta, ingrese 'C' o 'K' ")