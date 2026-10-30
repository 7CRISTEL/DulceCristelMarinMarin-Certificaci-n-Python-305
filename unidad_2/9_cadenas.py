# Cadenas y concatenacion con (+)
cadena1='Hola'
cadena2="Mundo"
multilinea="""Esto es una cadena
de varias lineas"""
print(cadena1 + cadena2 + multilinea)
#cadenas y repeticion
eco="ja"*3
print(eco)
#Cambiar una cadena de minuscula a mayuscula
tu_nombre='Cristel'
print(tu_nombre.upper())
#Cambiar una cadena de mayuscula a minuscula 
print(tu_nombre.lower())
#Remplaza texto en una cadena
frase="Me gusta programacion"
print(frase.replace("programacion","comunicacion"))
#Formato de concadenar cadenas con valores (F-String)
edad=16
nombre='Cristel'
mensaje=f"Hola, me llamo {nombre} y tengo\n{edad}años"
print(mensaje)
#Contar los caracteres de una cadena 
texto= "¡Felicidades por aun continuar en el CECY!!!"
cantidad_caracteres=len(texto)
print(cantidad_caracteres)
#Comprobar si un texto contiene una palabra 
oracion="Aprender python es divertido"
if "python" in oracion:
    print("Encontrado")
else:
    print("No esta")
#validar contenido de una cadena 
ncadena="aaa"
print(ncadena.isalpha())
print(ncadena.isdigit())