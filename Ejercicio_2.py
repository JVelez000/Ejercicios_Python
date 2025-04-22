while True:
  numero = input("Ingresa un número: ")
  try:
    numero = float(numero)
    if numero > 0:
      print("El número es positivo")
      break
    elif numero < 0:
      print("El número es negativo")
      break
    else:
      print("El número es cero")
      break
  except ValueError:
    print("Por favor, introduce un número válido")
