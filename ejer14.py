#Escribir un programa que pida al usuario un número 
# entero positivo y no permita continuar hasta que el
# usuario introduzca un número mayor que 0.

while True:
    numero= int(input("Introduce un número entero positivo mayor que 0: "))
    if numero>0:
        break
    print("El número tiene que ser mayor que 0. Inténtelo otra vez")
    
print("Has introducido el número: ", numero)