try:
#Ejemplo uno sin manejo de excepciones
    numero1=float(input("Ingresa el primer numero: "))
    numero2=float(input("Ingresa el segundo numero: "))
    resultado=numero1/numero2
    print(resultado)
except ZeroDivisionError:
    print("division entre cero fallida")
except ValueError:
    print("solo introduce NUMEROS MENSOOOOOO")