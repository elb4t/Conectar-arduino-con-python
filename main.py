#!/usr/bin/python
# -*- coding: utf-8 -*-
####################################
#            Autor: elb4t          #
####################################

import puertoArduino
from MedidorTemperatura-Humidad.mainMedidor import *

class main():
	def __init__():
		encontrado, puerto, conSerial = puertoArduino.buscaPuerto()
		if encontrado:
			# Si ha conectado con arduino empieza el programa
			print('el puerto del arduino es: ' + '/dev/ttyUSB' + str(puerto))
			mainMedidor(conSerial)
		else
			# Si no ha conectado con arduino se termina el programa
			print('No se ha encontrado Ardunio')
	
main()