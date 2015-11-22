#!/usr/bin/python
# -*- coding: utf-8 -*-
####################################
#            Autor: elb4t          #
####################################

# Este método búsca automaticamente el puerto de arduino
# y devuelve TRUE si lo a encontrado y FALSO cuando no lo encuentra

def buscaPuerto():
    # Varialbe para saber si hemos encontrado el puerto o no
    bEncontrado = False
    # Hacemos un bulce para recorrer los puertos que queremos comprobar
    for iPuerto in range(0, 4):
        try:
            # Puerto que vamos a probar
            PUERTO = '/dev/ttyUSB' + str(iPuerto)
            # Velocidad 
            VELOCIDAD = '9600'
            # Probamos ha abrir el puerto
            Arduino = serial.Serial(PUERTO, VELOCIDAD)
            # si no se ha producido un error, cerramos el puerto
            Arduino.close()
            # cambiamos el estado del la variable para saber si lo hemos encontrado
            bEncontrado = True
            # Salimos del bucle
            break
        except:
            # Si hay error, no hacemos nada y continuamos con la busqueda
            pass
    return bEncontrado, iPuerto
pass