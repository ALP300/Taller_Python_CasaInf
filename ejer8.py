#Escribir un programa que pregunte al usuario una cantidad a invertir, el
#interés anual y el número de años, y muestre por pantalla el capital
#obtenido en la inversión cada año que dura la inversión.

cantidad= float(input("Cantidad a invertir: "))
interes_anual= float(input("Interés anual: "))
años= int(input("Número de años: "))

for año in range (1,años+1):
    cantidad+=cantidad*interes_anual
    print("El año :", año, "la cantidad fue: ",cantidad)
    