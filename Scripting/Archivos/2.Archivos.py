#With

with open('Scripting/Archivos/Texto.txt', 'r+') as miArchivo:

    print(miArchivo.read())
    miArchivo.write('\n Texto escrito desde mi script ')
    miArchivo.seek(0)
    print(miArchivo.read())
    