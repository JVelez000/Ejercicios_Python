print("Escribe un año")
entrada = input(" ")

if entrada.isnumeric():
  año = int(entrada)

  if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    print(str(año) + " Es un año bisiesto :)")
  else:
    print(str(año) + " No es un año bisiesto :(")
else:
  print("Ingresa un numero valido / caracter numerico")