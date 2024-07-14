#Escribe un programa que solicite al usuario tres números y determine
#cuál de ellos es el mayor.
num1= float(input("Número 1: "))
num2= float(input("Número 2: "))
num3= float(input("Número 3: "))

if num1>num2 and num1>num3:
    print(f"{num1} es el mayor.")
elif num2>num3 and num2>num1:
    print(f"{num2} es el mayor.")
else:
    print(f"{num3} es el mayor.")