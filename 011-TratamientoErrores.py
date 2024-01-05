def divide(num1, num2):
    try:                      # intenta realizar la siguiente operaccion, si lo consigue, ignora el except
        return num1/num2
    except ZeroDivisionError: #si no lo consigue, hace lo siguiente y continua con el codigo
        return("Operación erronea")


while True:
    try:
        num1=int(input("Introduzca el primer numero  "))
        num2=int(input("Introduce el segundo numero  "))
        break
    except ValueError:
        print("Introduzca solo numeros enteros, vuelva a intentarlo")
    #except:
        #se pueden concatenear tratamientos de errores, si no se especifica el tipo de error, entonces es generico
    
    finally:
        print(".")  #lo que se encuentra dentro del finally se ejecutara siempre

print(divide(num1,num2))
