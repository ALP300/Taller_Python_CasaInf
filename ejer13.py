#Escribir un programa que pida al usuario un número entero positivo 
# y muestre por pantalla la suma de todos los números desde 1 hasta ese número.
numero= int(input("Introduce el número entero positivo: "))
suma=0
i=1
while i<=numero:
    suma+=i
    i+=1
    
print("La suma es: ", suma)
