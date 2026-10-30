alumnos = []
promedios = []

cantidad = int(input("Cuantos alumnos deseas agregar a tu lista: "))

for i in range(cantidad):
    nombre = input(f"Ingresa el nombre del alumno {i+1}: ")
    alumnos.append(nombre)

print("\nTu lista de alumnos es: ")
print(alumnos)

print()
for i in range(cantidad):
    promedio = float(input(f"Ingresa el promedio de {alumnos[i]}: "))
    promedios.append(promedio)

print("\nTu lista de promedios es: ")
print(promedios)

promedio_alto = promedios[0]
promedio_bajo = promedios[0]

for calif in promedios:
    if calif > promedio_alto:
        promedio_alto = calif
    if calif < promedio_bajo:
        promedio_bajo = calif

indice_alto = promedios.index(promedio_alto)
indice_bajo = promedios.index(promedio_bajo)

print(f"\nEl promedio mas alto es {promedio_alto} del alumno {alumnos[indice_alto]}")
print(f"El promedio mas bajo es {promedio_bajo} del alumno {alumnos[indice_bajo]}")