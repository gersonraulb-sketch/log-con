n1 = int(input("Ingrese el primer número: "))
n2 = int(input("Ingrese el segundo número: "))

if n1 == n2:
    print("Los números son iguales.")
elif n1 + n2 > 100:
    print("La suma de los números es mayor a 100.")
else:
    print("Los números son diferentes y su suma no supera 100.")