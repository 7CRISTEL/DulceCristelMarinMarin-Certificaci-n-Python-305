colores = ["rojo", "azul", "rosa", "negro", "amarillo", "verde"]
color=input("Ingresa el color: ")
encontrado=False
for contador in colores:
    print(contador)
    #si el color actual es "Rojo", detener el bucle
    if contador==color:
        print("Color esncontrado! saliendo del bucle")
        encontrado=True
        break
if not encontrado :
    print("El color,",color, "no se encontro")
