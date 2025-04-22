print("Ingresa el valor de la cuenta ")
valor=float(input(":"))
print("cuanto desea el cliente dejar de propina: 10%, 15%, 20%")
prop=float(input(":"))
if prop==10:
	result = valor * (prop/100)+valor
	print(result)
elif prop==15:
	result = valor * (prop/100)+valor
	print(result)
elif prop==20:
	result = valor * (prop/100)+valor
	print(result)