import math as mt
# La librería MATH contine la función SQRT(Raiz Cuadrada)

print('\n \t Solución Ecuación 2do Grado \n')
a= int(input('Ingrese la variable A '))
b= int(input('Ingrese la variable B '))
c= int(input('Ingrese la variable C '))

print('Los números que ingresaste son:\t','A=', a ,'\t','B=', b,'\t','C=', c)


sol1 = (-b + mt.sqrt(b**(2)+(4*a*c)))/(2*a)
sol2 = (-b - mt.sqrt(b**(2)+(4*a*c)))/(2*a)
print(' La solución 1 es:',round(sol1,2),'\n','La solución 2 es:', round(sol2,2), '\n')
