try:
    alumnos = ["Paola", "Daniel", "Angel", "Lucero", "Eduardo", "Estefanie"]
    calificaciones = [8, 10, 6, 8, 10, 8]

    print("Lista de alumnos y calificaciones")
    print(alumnos[0], calificaciones[0])
    print(alumnos[1], calificaciones[1])
    print(alumnos[2], calificaciones[2])
    print(alumnos[3], calificaciones[3])
    print(alumnos[4], calificaciones[4])
    print(alumnos[5], calificaciones[5])

    print("Indices impares:")
    print(1, 3, 5)

except IndexError:
    print("Error: El indice esta fuera del rango de la lista")

