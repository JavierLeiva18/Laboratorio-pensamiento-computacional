print("Semana No. 12- Ejercicio 2")

# Coordenadas iniciales del objeto
x = 0
y = 0

def menu():

  print("/nMenu:")
  print("a. Subir")
  print("b. Bajar")
  print("c. Ir a la derecha")
  print("d. Ir a la izquierda")
  print("e. Salir")

def mover_hacia_arriba():

  global y
  y += 1

def mover_hacia_abajo():

  global y
  y -= 1

def mover_hacia_la_derecha():

  global x
  x += 1

def mover_hacia_la_izquierda():

  global x
  x -= 1

def mostrar_coordenadas_finales():

  print(f"Coordenadas finales del personaje: {x},{y}")

while True:
  menu()
  opcion = input("Seleccione una opción: ")

  if opcion == "a":
    mover_hacia_arriba()
  elif opcion == "b":
    mover_hacia_abajo()
  elif opcion == "c":
    mover_hacia_la_derecha()
  elif opcion == "d":
    mover_hacia_la_izquierda()
  elif opcion == "e":
    mostrar_coordenadas_finales()
    break
  else:
    print("Opción no válida.")

print("¡Gracias por jugar!")