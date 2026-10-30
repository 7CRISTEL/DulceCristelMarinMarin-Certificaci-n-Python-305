# Ciclo externo para el numero de la base de la tabla 
for i in range(1,4):
    print(f"---Tabla del {i}")
    #Ciclo interno para multiplicar de 1 al 10
    for j in range(1,11):
    # 1(i) x1(j)=1
         print (f"{i} x {j} = {i*j}")
    print("Aqui termina la tabla del {i}")
    #Aqui termina el ciclo externo
    


