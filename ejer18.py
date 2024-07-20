#Ejercicio 6: Verificar si una cadena es un palíndromo
#Escribe una función que tome una cadena como argumento 
#y devuelva True si la cadena es un palíndromo 
#(se lee igual de adelante hacia atrás) 
#y False en caso contrario.

def palindromo(cadena):
    cadena= cadena.replace(" ","").lower()
    return cadena == cadena[::-1]
    
cadena= input("Introduce una cadena: ")
if palindromo(cadena):
    print("Es palindromo")
else:
    print("No es")
#Hola a todos soy leo
#holaatodossoyleo
