usuario = 'user1234'
contraseña = '12345678'

usu = input('Ingrese su usuario: ')
cont = input('Ingrese su contraseña: ')

if usu == usuario and cont == contraseña:
    print('Acceso concedido')
else:
    print('Acceso denegado')