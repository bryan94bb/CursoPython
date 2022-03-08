#Iteraciones
# FOR es una instrucción que permite recorrer un iterable

listafrutas = ['Pera', 'Manzana','Banano']

for i in  listafrutas:
    print(i)

#FOR en rangos númericos
for num in range(0,5):
    print(num)

#for num in range(0,5):
#    print('Elemento {}'.format(item))

matriz = [
    [0,1,0],
    [1,1,1],
    [0,0,2]
]
#print(matriz)

for fila in matriz:
    for columna in matriz:
        print(columna)
