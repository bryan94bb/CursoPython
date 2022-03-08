from turtle import color


class Carro:
    def __init__(self,placa='ABC-123', color='rojo'):
        self.placa = placa,
        self.color = color

    def rodar(self):
        print(f'Soy el auto de placas {self.placa} y soy de color {self.color}')

carro1= Carro()
carro1.rodar()
carro2 = Carro(placa='PBZ-7260', color='blanco')
carro2.rodar()