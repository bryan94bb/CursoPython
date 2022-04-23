
class Personaje:
    # init -> inicializar atributos
    def __init__(self, nombre= 'Juan'):
        self.nombre = nombre
        self.cualidades = ['Bueno', 'Justo', 'Sincero']
    def saludar(self):
        print('Hola')

    def __str__(self) -> str:
        return f'Clase Personaje, el nombre es {self.nombre}'
    def __getitem__(self, i):
        return self.cualidades[i]
    

personaje = Personaje()
print(personaje.__str__())
print(personaje.__getitem__(2))
