
class Coche():
    def __init__(self): #Metodo contructor
        self.largo=250
        self.ancho=120
        self.__ruedas=4 # __palabra = encapsulada, encapsular: no permitir modificar una propiedad desde fuera de la clase
        self.movimiento=False

    def arrancar(self):
        self.movimiento=True

    def parar(self):
        self.movimiento=False

    def estado(self):
        if (self.movimiento):
            print("Coche en marcha", end=" ")
        else:
            print("Cohe parado", end=" ")
        print(self.__ruedas)

    def __chequeo(self):    # encapsulado, no se puede acceder desde fuera
        print("Chequeo: ")
        self.gasolina="Ok"
        self.aceite="Ok"
        self.puertas="cerradas"

        if(self.gasolina=="Ok"and self.aceite=="Ok" and self.puertas=="cerradas"):
            return True
        else:
            return False

    def check(self):
        che=self.__chequeo()    #solo se puede accedder al metodo encapsulado desde dentro de la propia clase
        print(che)

miCoche=Coche()
print(miCoche.movimiento, miCoche.ancho)
miCoche.estado()
miCoche.arrancar()
miCoche.__ruedas=2  #al estar fuera de la clase, no puedo modificar el valor de una propiedad encapsulada
miCoche.estado()
miCoche.parar()
miCoche.estado()
#print(miCoche.__chequeo())  dará error
miCoche.check()