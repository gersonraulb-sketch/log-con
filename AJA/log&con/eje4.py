n = int(input("Ingrese un número: "))

if n > 9 and not n > 20:
    print("El número esta en rango de 10 a 20.")
elif n > 29 and not n > 40:
    print("El número esta en rango de 30 a 40.")
else:
    print("El número no cumple ninguna de las condiciones.")