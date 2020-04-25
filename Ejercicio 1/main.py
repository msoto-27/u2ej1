from random import randrange, choice
from clases.email import Email
from clases.manejador import Manejador

if __name__ == '__main__':
    #Inciso 1
    print('Ingrese su nombre')
    nombre = input()
    print('Ingrese su id de cuenta')
    dir = input()
    print('Ingrese su dominio')
    dom = input()
    print('Ingrese el tipo de dominio')
    tipo_dom = input()
    print('Ingrese una contraseña')
    co = input()
    e = Email(dir, co, dom, tipo_dom)
    print('Estimado {} te enviaremos tus mensajes a la dirección {}'.format(nombre, e.retornaEmail()))
    #Inciso 2
    print('Introduzca su contraseña actual')
    e.cambiarContraseña(input())
    #Inciso 3
    print('Ingrese una direccion de correo')
    dirIngresada = input()
    e2 = Email()
    e2.crearCuenta(dirIngresada)
    #Inciso 4
    lista = Manejador()
    lista.leerDirecciones()
    lista.registrarEmails()
    print('Ingrese un dominio')
    domIngresado = input()
    print('Cantidad de direcciones con el dominio ', domIngresado, ': ', lista.contarDominio(domIngresado))
    
  
    """print('Testing direcciones')
    
    for i in range(0, 10):
        direccion_aleatoria = ''
        for j in range(randrange(5, 10)):
            direccion_aleatoria += chr(randrange(97, 122))
        if(randrange(0, 4)):
            direccion_aleatoria += '@'
        direccion_aleatoria += chr(randrange(97, 122)) + 'mail'
        if (randrange(0, 4)):
            direccion_aleatoria += '.'
        direccion_aleatoria += choice(['com', 'edu', 'ar'])
        print(direccion_aleatoria)
        email_aleatorio = Email()
        email_aleatorio.crearCuenta(direccion_aleatoria)
        """
