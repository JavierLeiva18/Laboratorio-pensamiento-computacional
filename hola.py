def calcular_serie(n):
    if n <= 0:
        print("El número debe ser mayor que 0.")
        return None
    
    suma = 0
    for i in range(1, n + 1):
        suma += 1 / i
    
    return suma

# Solicitar al usuario el valor de N
N = int(input("Ingrese un número entero mayor que 0: "))

# Calcular la serie
resultado = calcular_serie(N)

# Imprimir el resultado si no es None
if resultado is not None:
    print("Resultado de la serie (1/1) + (1/2) + (1/3) + ... + (1/N):", resultado)