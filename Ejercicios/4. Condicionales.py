# Solcitar al usuario que ingrese por teclado un texto le vamos a indicar si lo ingresa es o 
# no un palíndromo 
# (palindromo es expresión que es igual si se lee de izquierda a derecha que de derecha a izquierda.)

print('\n\tIdentificador de palíndromos')
texto = str(input('Ingrese una cadena de texto:\t'))
print('\nPalabra de izquierda a derecha:\t '+texto)
print('Palabra de derecha a izquierda:\t '+texto[::-1]+'\n')
if texto == texto[::-1]:
    print('Felicidades, Ingresaste un palíndromo!!!')
elif texto.lower() == texto[::-1].lower():
    print('Palíndromo, ignorando las mayúsculas')
elif texto.replace(' ','') == texto[::-1].replace(' ',''):
    print('Palíndromo ignorando las mayusculas y los espacios')
elif texto.lower().replace(' ','') == texto[::-1].lower().replace(' ',''):
    print('Palíndromo ignorando las mayúsculas y los espacios')
else:
    print('No ingresaste un palíndromo')