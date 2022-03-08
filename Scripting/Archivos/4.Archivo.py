# 1. Crear un Script que genere un archivo con elementos repetidos

import random

deportes = ['Futbol','Tenis','Basquet','Balonmano']
#for i in range (100):
#    print(random.choice(deportes))

#Creación de Archivo
#archivo = open('Scripting/Archivos/Texto2.txt','w')
#archivo.close()

with open('Scripting/Archivos/Texto2.txt', mode='r+') as miArchivo:
    for i in range(500):
        miArchivo.write(str(random.choice(deportes)+'\n'))


#Crear un nuevo archivo 
with open('Scripting/Archivos/Texto2.txt', mode='r+') as miArchivo:
    linea = miArchivo.readlines()
p1=linea.count("Futbol\n")
p2=linea.count("Tenis\n")
p3=linea.count("Basquet\n")
p4=linea.count("Balonmano\n")

with open('Scripting/Archivos/Resumen.txt','w+') as Resumen:
    Resumen.write('DEPORTE \tCANTIDAD\n')
    Resumen.write(f'Futbol: \t{p1} \n')
    Resumen.write(f'Tenis: \t\t{p2} \n')
    Resumen.write(f'Basquet: \t{p3} \n')
    Resumen.write(f'Balonmano: \t{p4} \n')
    Resumen.write(f'TOTAL:\t \t{p1+p2+p3+p4}')
