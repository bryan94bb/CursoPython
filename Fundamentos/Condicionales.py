# Si, sino, entonces
# if, else, elif (ifelse)

variable1 = True
variable2 = False

#print('Hola'=='Hola')

if variable1 and variable2 == True:
    print ('La expresión es verdadera') 
else:
    print('La expresión es falsa')


#Ejercicio de Condicionales
#Palindromo

texto = input('Ingrese el texto: ')
print('Palabra de izquierda a derecha: '+ texto)
print('Palabra de izquierda a derecha: '+ texto[::-1])
if texto == texto[::-1]:
    print('ingresaste un palindromo')
elif texto.lower()== texto[::-1].lower():
    print('Palindromo ignorando las mayusculas')

nombre = Bryan
