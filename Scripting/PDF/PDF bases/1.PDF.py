import PyPDF2 as pdf

with open('C:/Users/bryan94bb/Desktop/CursoPython2/Scripting/PDF/PDF bases/marcaAgua.pdf', 'rb') as miArchivo:
    print(miArchivo)
    print(type(miArchivo))
    #La información está en BINARIO, debo abrir esta info en otro formato
    archivoPDF= pdf.PdfFileReader(miArchivo)
    print(archivoPDF)
    print(type(archivoPDF))
    