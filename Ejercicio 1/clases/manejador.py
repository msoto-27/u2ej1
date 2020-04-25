import csv

import re

from clases.email import Email

class Manejador:
    def __init__(self):
        self.__listaDirecciones = []
        self.__listaEmails = []
    def leerDirecciones(self):
        archivo = open('correos.csv')
        reader = csv.reader(archivo, delimiter = ',')
        for correo in reader:
            self.__listaDirecciones.append(correo[0])
            
        print('Lista de direcciones: ', self.__listaDirecciones)
    def registrarEmails(self):
        for i in range(len(self.__listaDirecciones)):
            if re.match(r"[a-z, 0-9]{1,20}@[a-z]{1,10}\.[a-z]{1,6}", self.__listaDirecciones[i]):
                self.__listaEmails.append(Email())
                self.__listaEmails[len(self.__listaEmails)-1].crearCuenta(self.__listaDirecciones[i])
    def contarDominio(self, dominio):
        c = 0
        for i in range(len(self.__listaEmails)):
            if (self.__listaEmails[i].getDominio() == dominio):
                c += 1
        return c
                
