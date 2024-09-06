def crearmatriz(row, column):

    matriz= [[0 for c in range (column)]for f in range(row)]

    

    for f in range(len(matriz)):
        for c in range(len(matriz[0])):

            nro= int(input('Ingrese un numero para la matriz: '))

            matriz[f][c]=nro


    return matriz

def ordenarfilas():

    '''for f in range(len(matriz)):
        for c in range(len(matriz[0])):
            pass
        if matriz[f]>matriz[f+1]:
            listaux=
    '''
    for fila in matriz:
        fila.sort()

    return matriz   




filas = int(input('Ingrese el numero de filas: '))
columnas = int(input('Ingrese el numero de columnas: '))


matriz= crearmatriz(filas,columnas)

for fila in matriz:
    for elemento in fila:
        print('%3d' %elemento, end='')
    print()

matriz= ordenarfilas()

print('')

for fila in matriz:
    for elemento in fila:
        print('%3d' %elemento, end='')
    print()




