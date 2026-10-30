promedio = [9, 8, 7, 6, 10]
#1. encontrar el promedio mas alto usando el ciclo for
#suponemos inicialmente que el promedio mas alto es el primer elemento  
promedio_alto=promedio[0]
promedio_bajo=promedio[0]
for contador in promedio:
    if contador>promedio_alto:
        promedio_alto=contador

    if contador<promedio_bajo:
        promedio_bajo=contador





print("El promedio mas alto es", promedio_alto)
print("El promedio mas bajo es", promedio_bajo)