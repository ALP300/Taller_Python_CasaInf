#Ejercicio 5: Calcular la suma de una lista de números
#Escribe una función que tome una lista de números y devuelva su suma.

def calcular_suma(list_num):
    suma=0
    for numero in list_num:
        suma+=numero
    return suma
        

numeros=[1,2,3,4,5,6]
suma= calcular_suma(numeros)
print("La suma de los números es: ", suma)
