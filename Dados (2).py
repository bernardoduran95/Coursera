import random

respuesta = input("Desea lanzar los dados?(si/no): ") 
suma = 0

while respuesta == 'si' or respuesta == 'SI':

    n1 = random.randint(1,6)
    n2 = random.randint(1,6)
    suma = n1 + n2
    print("Lanzamiento N°1: ", n1)
    print("Lanzamiento N°2: ", n2)
    print("La suma de los lanzamientos es: ", suma)
    
    respuesta = input("Desea seguir lanzando los dados?: ")

else:
    print("Fin del Programa")

