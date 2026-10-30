#Creando un diccionario en python 
persona={
    "nombre":"Cristel",
    "edad": 16,
    "profecion":"ingenieria",
    "estudiante":False
}
print(persona)
#Accediendo a un valor en especifico
print(persona["profecion"])
#Se puede usar el metodo .get
#Es util porque no da eeror si la clave no existe
persona["edad"]=16
print(persona.get("edad"))
#Agregar un par(clave:valor)
persona["ciudad"]="San pepe ranch"
print(persona)
#Recorrer un diccionario con un bucle
for clave,valor in persona.items()
print(f"{clave}:{valor}")
