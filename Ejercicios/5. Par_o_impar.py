# Usuario ingrese un número y le diremos si es par o impar

numero = int(input('Ingresa un número: '))
# % Modulo o Residuo
if numero%2 == 0:
    print('Es un número par\n')
else:
    print('Es un número impar\n')

if numero>0:
    print('Es un número mayor a cero\n')
else:
    print('Es un número menor a cero\n')