#Escribe un programa que tome una 
# calificación numérica de un
#estudiante (entre 0 y 100) y le asigne 
# una letra según la siguiente tabla:
#- 90-100: A
#- 80-89: B
#- 70-79: C
#- 60-69: D
#- Menos de 60: F
calificacion= float(input("Ingrese la calificación: ")) #84
if calificacion>=90:
    letra='A'
elif calificacion>=80:
    letra='B'
elif calificacion>=70:
    letra='C'
elif calificacion>=60:
    letra='D'
else:
    letra='F'

print("La letra correspondiente es:"+ letra)
