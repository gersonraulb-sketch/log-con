nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))

print(f"Hola, {nombre}. Tienes {edad} años.")

if edad > 18:
    print("Eres mayor de edad.")
elif edad == 18:
    print("Acabas de cumplir la mayoría de edad.")
else:
    print("Eres menor de edad.")