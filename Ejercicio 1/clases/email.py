import re

class Email:
    __idCuenta = ''
    __dominio = ''
    __tipoDominio = ''
    __contraseña= ''
    def __init__(self, idCuenta = '', contraseña = '', dominio = '', tipoDominio = ''):
        self.__idCuenta = idCuenta
        self.__dominio = dominio
        self.__tipoDominio = tipoDominio
        self.__contraseña = contraseña
    def retornaEmail(self):
        return('{}@{}.{}'.format(self.__idCuenta, self.__dominio, self.__tipoDominio))
    def getDominio(self):
        return(self.__dominio)
    def crearCuenta(self, direccion, contraseña = ''):
        auxiliar = re.match(r"[a-z, 0-9]{1,20}@[a-z]{1,10}\.[a-z]{1,6}", direccion)
        if(auxiliar):
            a, b = direccion.split('@')
            b, c = b.split('.')   
            self.__idCuenta = a
            self.__dominio = b
            self.__tipoDominio = c
            self.__contraseña = contraseña
        else:
            print('Direccion no valida')
    def cambiarContraseña(self, ingresada):
        if ingresada == self.__contraseña:
            print('Introduzca su nueva contraseña')
            self.__contraseña = input()
        else:
            print('Contraseña incorrecta') 
