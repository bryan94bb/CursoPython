from abc import ABC, abstractmethod

#Interaces -> SOLO métodos, donde no especifico la implementación.
# Para poder tener una interfaz necesariamente 
class Animal(ABC):
    @abstractmethod
    def darInformacion(self):
        pass

class Mamifero(Animal):
    def saludar(self):
        print('Hola')
    def darInformacion(self):
        print ('Me alimento de leche')

class Reptil(Animal):
    def darInformacion(self):
        print('Soy de sangre fría')

mamifero = Mamifero()
mamifero.darInformacion()
mamifero.saludar()
culebra = Reptil()
culebra.darInformacion()
