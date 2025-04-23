import random

numero = random.randint(1, 10)
adivina = int(input("Adivina el número (entre 1 y 10): "))

if adivina == numero:
  print("¡Correcto! adivinaste el numero")
elif adivina < numero:
  print("Tu numero es mas bajo, intenta con uno mas alto")
else:
  print("Tu numero es mas alto, intenta con uno mas bajo")

print(f"(El numero era {numero})")
