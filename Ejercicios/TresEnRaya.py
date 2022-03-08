#Tres en Raya

#Se terminará el juego cuando se marque 3 en linea
#Se presenta un menu al inicio en el que se pueda ingresar los nombres

global nombrejugador1
nombrejugador1 = 'Jugador 1'
global nombrejugador2
nombrejugador2 = 'Jugador 2'
global piezajugador1
piezajugador1 = 'X'
global piezajugador2
piezajugador2 = 'O'

def menu ():
    print('\n \t Tres en raya \n')
    print('1. Ingrese el nombre de los jugadores:')
    print('2. Seleccionar piezas de jugadores:')
    print('3. Jugar')
    print('4. Salir')
    opcion = input('Ingrese una opción: \t')
    print('\t',opcion)
    return opcion

def nombrejugadores():
    print ('Nombre de Jugadores \n')
    print ('1. Cambiar del J1 \n')
    print ('2. Cambiar del J2 \n')
    opcionnombre = input('A cuál jugador va a cambiar el nombre: 1 o 2: \t')
    if opcionnombre == '1':
        global nombrejugador1
        nombrejugador1 = input('Ingrese el nombre 1 \t')
    elif opcionnombre == '2':
        global nombrejugador2
        nombrejugador2 = input('Ingrese el nombre 2 \t')    
    else:
        print('Por favor ingrese una opción válida\n')
    print('J1:',nombrejugador1,'\t', 'J2:', nombrejugador2)

def cambiarpiezas():
    print ('Piezas de los Jugadores ')
    print ('1. Cambiar la pieza del J1 \n')
    print ('2. Cambiar la pieza del J2 \n')
    opcionpieza = input('A cuál jugador va a cambiar la pieza: 1 o 2: \t')
    global piezajugador1
    global piezajugador2
    if opcionpieza == '1':
        auxpieza1 = input('Ingrese la pieza 1 \t')
        if auxpieza1 != piezajugador2:
            global piezajugador1
            piezajugador1 = auxpieza1
        else:
            print('La pieza ingresada es igual a la del J2')
    elif opcionpieza == '2':
        auxpieza2 = input('Ingrese la pieza 2 \t') 
        if auxpieza2 != piezajugador1:
            piezajugador2 = auxpieza2   
        else:
            print('La pieza ingresada es igual a la del J1')       
    else:
        print('Por favor ingrese una opción válida\n')
    print('Pieza 1:',piezajugador1,'\t Pieza 2:', piezajugador2)

def jugar():
    print('Es turno del jugador \t', nombrejugador1)
    print('Es turno del jugador \t', nombrejugador2)
    
def main():
    terminarjuego = False
    while terminarjuego == False:
        opcionMenu = menu() #va a ejecutar la opción menú, se queda con el retorno (return)
        if opcionMenu == '1':
            nombrejugadores()
        elif opcionMenu == '2':
            cambiarpiezas()
        elif opcionMenu == '3':
            print ('Jugando')
        elif opcionMenu == '4':
            print ('\n \tGracias por Jugar')
            terminarjuego = True
        else:
            print('Por favor ingrese una opción válida\n')
            menu()

main()
