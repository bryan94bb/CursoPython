#Conjuntos o Set
# Un CONJUNTO es con LLAVES
conjunto1 = {1,2,3,4}
print (conjunto1)

cA = {1,2,3,4,5,6,7}
cB = {3,4,5, 11}

#Agregar un elemento con  .add()
cA.add(8)
print(cA)

#Averiguar el tamaño (cardinalidad)
print(len(cA))

#Eliminar 
cA.discard(8)
print(cA)

#Agregar varios elementos - Update conjunto
cA.update({8,9})
print(cA)

#Métodos entre conjuntos
print('Conjunto A:', cA)
print('Conjunto B:', cB)
# cA 1,2,3,4,5,6,7,8,9
# cB 3,4,5

#Diferencia
print(cA.difference(cB))
# 1,2,6,7,8,9

#Unión
cC={10}
print(cA.union(cC))
#  1,2,3,4,5,6,7,8,9,10

#Intersección
print(cA.intersection(cB))
# 3,4,5

#Diferencia Simétrica
print('Diferencia Simétrica', cA.symmetric_difference(cB))

