#Ejercicio 1: Calcular el área de un círculo
#Escribe una función que calcule y devuelva el área de un círculo dado su radio.
import math

def calcular_area_circulo(r):
    area= math.pi*r**2
    return area
    

radio= float(input("Introduce el radio del círculo: "))
area= calcular_area_circulo(radio)

print("El área es: ", area)

