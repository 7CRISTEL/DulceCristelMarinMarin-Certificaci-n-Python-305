#Creando una matriz
matriz=[
    [5,8,1,6],#Fila 1 x3 columnas
    [3,9,2,4]#Fila 2 x3 columnas
] 
#Obteniendo el numero total de filas y columnas 
#filas=len(matriz)
#columnas=len(matriz[0])
#Ciclo externo para los indicees de las filas
for i in range(0,2):
    #Ciclo interno  para  los indices de las columnas
    for j in range(0,3):
        print(f"posicion[{i}][{j}]={matriz[i][j]}")