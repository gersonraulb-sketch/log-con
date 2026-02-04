cc = input('¿Es ciudadano colombiano? (si/no): ')
if cc == 'si':
    edad = int(input('Ingrese su edad: '))
    if edad >= 18:
        print('Usted puede votar en las elecciones.')
    else:
        print('Es menor de edad, no puede votar.')
else:
    print('Usted no es ciudadano colombiano, no puede votar en las elecciones.')