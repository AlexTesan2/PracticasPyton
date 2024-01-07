"""comentario
compuesto 
por varias
lineas
"""
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
print(type(y))

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits

def myfunc():
    global x
    x = "fantastic"

myfunc()

print("Python is " + x)