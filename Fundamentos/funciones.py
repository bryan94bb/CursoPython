#funciones -> DEF
# A (regla de correspondencia) -> B
# A -> f() -> B

#Procedimiento: NO entrega ningún valor de vuelta
#"Función Vacia"


#Funciones: Recibe parámetros!
#
edades = (18, 5,20,22,17,14.5,2)

def esMayorEdad(edad: int):
    if edad >= 18:
        return True
    return False

for edad in edades:
    print(esMayorEdad(edad))

#3 Recibir varios parámetros
def saludar2(nombre, apellido):
    return f'Saludos {nombre} {apellido}'

print(saludar2('Jonathan','Buenaño'))

#3 Parámetros por defecto
def saludar3(nombre = 'Bryan', apellido = 'Buenaño'):
    return f'Saludos {nombre} {apellido}'

print(saludar3())
print(saludar3(nombre='Fernando'))
print(saludar3(apellido='Salazar'))
print(saludar3('Ismael','Bautista'))

def calcularCubo(numero:int):
    '''
    Permite calcular el cubo de un número
    - numero: número entero
    return: el cubo de un número
    '''
    return numero**3

print(calcularCubo(5))

#Para mostrar los comentarios de la función

print(calcularCubo.__doc__)

#FUNCIONES ARGS
#args


def listarAlumnos(*alumnos):
    print(f'Alumno: (alumnos)')

listarAlumnos('Anderson')
listarAlumnos('Anderson','Andrés', 'Bryan', 'Janeth')


