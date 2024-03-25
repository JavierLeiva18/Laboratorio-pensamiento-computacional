#Erick Javier Leiva León
#Número de carnet: 1146624
print("Semana 10: Ejercicio 1")
mes=int(input("Ingrese un número entre 1 y 12: "))
#validando con if-else,elif
if mes<1 or mes>12: 
    print("Error: el número a ingresar debe ser entre 1 y 12")
else:
    if mes==1:
        print("Mes: Enero")
    elif mes==2:
        print("Mes: Febrero")
    elif mes==3:
        print("Mes: Marzo")
    elif mes==4:
        print("Mes: Abril")
    elif mes==5:
        print("Mes: Mayo")
    elif mes==6:
        print("Mes: Junio")
    elif mes==7:
        print("Mes: Julio")

#Validando con case
match(mes):
    case 1: 
        print("Mes: Enero")
    case 2:
        print("Mes: Febrero")
    case 3:
        print("Mes: Marzo")
    case _:
        print("Es otro mes")

print()

print("Semana No. 10: Ejercicio 2")

a=int(input("Ingresar un primer número mayor a 0: "))
b=int(input("Ingresar un segundo número mayor a 0: "))
c=int(input("Ingresar un tercer número mayor a 0: "))

if a<=0 or b<=0 or c<=0:
    print("Error, ingresar números mayor a 0")
if a>b:
    if a>c:
        print("A es el mayor")
    else:
        if a==c:
            print("A es mayor a B, pero igual a C")
        else:
            print("A es mayor a B, pero menor que C")
elif a==b:
    if a>c:
        print("A es igual a B, pero mayor que C")
    else:
        if a==c:
            print("A,B y C son iguales")
        else:
            print("A es igual a B, pero menor que C")
elif b>c:
    print("B es mayor a A y mayor que C")
else:
    if b==c:
        print("B es igual a C, pero mayor que A")
    else:
        print("B es mayor que A, pero menor que C")

print()

print("Semana No. 10: Ejercicio 3")

def calcular_signo_zodiacal(dia, mes):
    if (mes == 1 and dia >= 20) or (mes == 2 and dia <= 18):
        return "Acuario"
    elif (mes == 2 and dia >= 19) or (mes == 3 and dia <= 20):
        return "Piscis"
    elif (mes == 3 and dia >= 21) or (mes == 4 and dia <= 19):
        return "Aries"
    elif (mes == 4 and dia >= 20) or (mes == 5 and dia <= 20):
        return "Tauro"
    elif (mes == 5 and dia >= 21) or (mes == 6 and dia <= 20):
        return "Géminis"
    elif (mes == 6 and dia >= 21) or (mes == 7 and dia <= 22):
        return "Cáncer"
    elif (mes == 7 and dia >= 23) or (mes == 8 and dia <= 22):
        return "Leo"
    elif (mes == 8 and dia >= 23) or (mes == 9 and dia <= 22):
        return "Virgo"
    elif (mes == 9 and dia >= 23) or (mes == 10 and dia <= 22):
        return "Libra"
    elif (mes == 10 and dia >= 23) or (mes == 11 and dia <= 21):
        return "Escorpio"
    elif (mes == 11 and dia >= 22) or (mes == 12 and dia <= 21):
        return "Sagitario"
    else:
        return "Capricornio"

dia = int(input("Ingresar el día de tu fecha de nacimiento: "))
mes = int(input("Ingresar el mes de tu fecha de nacimiento (usar números): "))


signo_zodiacal = calcular_signo_zodiacal(dia, mes)

print("Su signo zodiacal es:", signo_zodiacal)  