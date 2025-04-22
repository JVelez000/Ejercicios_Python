import random

numero_secreto = random.randint(1, 10)
adivina = int(input("Adivina el número (entre 1 y 10): "))

if adivina == numero_secreto:
  print("¡Correcto! Adivinaste el número secreto.")
elif adivina < numero_secreto:
  print("Muy bajo. Intenta con un número más alto.")
else:
  print("Muy alto. Intenta con un número más bajo.")

print(f"(El número secreto era: {numero_secreto})")  # Puedes quitar esta línea si no quieres revelar el número
