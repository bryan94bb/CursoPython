import math

print('\n \t Solución Ecuación 2do Grado \n')
a= int(input('Ingrese la variable A  '))
b= int(input('Ingrese la variable B '))
c= int(input('Ingrese la variable C '))

print('Los números que ingresaste son:\t','A=', a ,'\t','B=', b,'\t','C=', c)


sol1 = (-b + math.sqrt(b**(2)+(4*a*c)))/(2*a)
sol2 = (-b - math.sqrt(b**(2)+(4*a*c)))/(2*a)
print(sol1, '\n', sol2)
print(type(sol1))