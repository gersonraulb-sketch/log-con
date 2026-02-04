numero =int(input("Ingrese un número entero: "))

if numero > 10:
    print('El número es mayor que 10.')
    if numero > 30:
        print('ademas el número es mayor que 30.')
    elif numero > 20:
        print('ademas el número es mayor que 20.')
        if True:
            print('Ejemplo')
    else:
        print('ademas el número es mayor a 21.')
else:
    print('El número es menor o igual a 10.')
        