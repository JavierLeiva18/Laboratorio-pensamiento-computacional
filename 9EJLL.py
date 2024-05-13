# Solicitar al usuario ingresar una cantidad en metros
metros = float(input("Ingrese la cantidad en metros: "))

# Realiza las conversiones utilizando estas equivalencias
millas = metros / 1609.34
kilometros = metros / 1000
pies = metros * 3.28
pulgadas = pies * 12

# Muestra los resultados
print("Resultado:")
print("Millas:", round(millas, 3))
print("Kilómetros:", round(kilometros, 2))
print("Pies:", round(pies, 2))
print("Pulgadas:", round(pulgadas, 2))