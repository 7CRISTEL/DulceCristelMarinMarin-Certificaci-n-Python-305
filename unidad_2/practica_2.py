calificaciones = []

cal1 = float(input("Calificación 1 (0-10): "))
calificaciones.append(cal1)

cal2 = float(input("Calificación 2 (0-10): "))
calificaciones.append(cal2)

cal3 = float(input("Calificación 3 (0-10): "))
calificaciones.append(cal3)

print("Tu lista es:", calificaciones)

promedio = (calificaciones[0] + calificaciones[1] + calificaciones[2]) / 3

print("Tu promedio es:", promedio)

if promedio >= 6:
    print("APROBADO")
else:
    print("REPROBADO")
