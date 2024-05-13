#Área de definición de funciones
import math 
def menu():
    print("Elija una opción: ")
    print("a. Área de triángulo")
    print("b. Área de cuadrado")
    print("c. Área de rectangulo")
    print("d. Área de círculo")
    opcion=input()
    return opcion
def ObtenerÁreaTriangulo(base, altura):
    return (base*altura)/2
def ObtenerÁreaCuadrado(lado):
    return(lado**2)
def ObtenerÁreaRectángulo(base, altura):
    return base*altura
def ObtenerÁreaCírculo(radio):
    return math.pi*radio**2

#Área de interacción con el usuario
print("Semana No.15 - Ejercicio 1")

match(menu()):
    case "a":
        print("El área del triángulo es:", ObtenerÁreaTriangulo(float(input("Ingrese la base del triángulo:")),float(input("Ingrese la altura del triángulo:"))))

    case "b":
        print("El área del cuadrado es:", ObtenerÁreaCuadrado(float(input("Ingrese la base del cuadrado:"))))

    case "c":
        print("El área del rectángulo es:", ObtenerÁreaRectángulo(float(input("Ingrese la base del rectángulo:")),float(input("Ingrese la altura del rectángulo:"))))

    case "d":
        print("El área del círculo es:", round(ObtenerÁreaCírculo(float(input("Ingrese el radio del círculo:"))),2))
