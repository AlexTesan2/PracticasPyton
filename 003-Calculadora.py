
num1=int(input("Introduzca  el primer numero: "))
num2=int(input("Introduzca el segundo numero: "))
operador=input("""Introduzca la operación deseada:
suma(s), resta(r), multiplicación(m), división(d), elevación(e):""").upper()

def suma(n1,n2):
    return n1+n2

def resta(n1,n2):
    return n1-n2

def multiplicacion(n1,n2):
    return n1*n2

def division(n1,n2):
    return n1/n2

def elevar(n1,n2):
    return n1**n2

if operador == "S" or operador=="+":
    resultado=suma(num1,num2)
elif operador=="R" or operador=="-":
    resultado=resta(num1,num2)
elif operador=="M" or operador=="*":
    resultado=multiplicacion(num1,num2)
elif operador=="D" or operador=="/":
    if num2==0:
        resultado="\nIndeterminación\n"
    else:
        resultado=division(num1,num2)
elif operador=="E" or operador=="**":
    resultado=elevar(num1,num2)
else:
    resultado="\nSe ha producido un error, vuelva a intentarlo\n"

print(resultado)