while True:
  edad = input("¿Cuál es tu edad? ")
  if edad.isnumeric():
      edad = int(edad)
      if edad > 0 and edad < 18:
        print("Eres menor de edad")
        break
      elif edad >= 18:
        print("Eres mayor de edad")
        break
  else:
      print("Por favor, introduce un caracter válido para la edad")
