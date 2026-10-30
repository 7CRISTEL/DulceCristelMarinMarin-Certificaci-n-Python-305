#1. creamos un diccionario
nuevo_usuario={}
#2. pedimos los datos desde el teclado
nuevo_usuario["nombre"]= input("Ingresa tu nombre: ")
nuevo_usuario["edad"]= int(input("Ingresa tu edad: "))
nuevo_usuario["estatura"]= float(input("Ingresa tu estatura en metros: "))
print("\n---Informacion guardada---")
#Mostrando la informacion del diccionario
print(nuevo_usuario)
