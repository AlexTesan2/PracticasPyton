class Vehiculos():
    def __init__(self, marca, modelo):
        self.marca=marca
        self.modelo=modelo
        self.enmarcha=False
        self.acelera=False
        self.frena=False
    
    def arrancar(self):
        self.enmarcha=True
    def acelerar(self):
        self.acelera=True
        self.frena=False
        self.enmarcha=True
    def frenar(self):
        self.acelera=False
        self.frena=True

    def estado(self):
        print("Marca:", self.marca, " Modelo:", self.modelo, "\nEn marcha: ",
        self.enmarcha, " Acelerando:", self.acelera, " Frenando:", self.frena)

class Moto(Vehiculos):  #indicamos que hereda de la clase Vehiculos
    pass

miMoto=Moto("Honda","CBR")
print(miMoto.enmarcha)
miMoto.arrancar()
miMoto.estado()