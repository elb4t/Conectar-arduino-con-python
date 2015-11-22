#!/usr/bin/python
# -*- coding: utf-8 -*-
####################################
#            Autor: elb4t          #
####################################

import time
import serial

class mainMedidor():

	def __init__(con):
		# Recogemos la conexión serial con arduino
		global conexArduino = con
		global s = True
		global _a = 1
		interface()
		obtenerDatos()
			

	def interface():
		app = Tk()
		app.title("Medidor de temperatura")

		#Ventana Principal

		vp = Frame(app)
		vp.grid(column=0, row=0, padx=(100,100), pady=(10,10))
		vp.columnconfigure(0, weight=1)
		vp.rowconfigure(0, weight=1)

		etiqueta = Label(vp, text="Temperatura")
		etiqueta.grid(column=1, row=1, sticky=(W,E))

		boton = Button(vp, text=str(t)+"ºc" , command = farent)
		boton.grid(column=2, row=1)

		etiqueta1 = Label(vp, text="Humitat")
		etiqueta1.grid(column=1, row=2, sticky=(W,E))

		boton1 = Button(vp, text=str(h)+"%")
		boton1.grid(column=2, row=2)

		boton2 = Button(vp, text="exit",command =app.destroy)
		boton2.grid(column=2, row=3)

		boton3 = Button(vp, text="stop", command = stop )
		boton3.grid(column=1, row=3)

		#etiqueta.pack()
		#boton.pack()
		app.mainloop() 

	def obtenerDatos():
		while True:
			flagCharacter = "k"

			# Retardo para establecer la conexión serial
			time.sleep(1.8) 
			conexArduino.write(flagCharacter)
			conexArduino.readline()
			datos = conexArduino.readline()
			datos1 = datos.split(",")
			h=datos1[0]
			t=datos1[1]
			print t
			t=float(t)
			farent()
			time.sleep(1.8) 
			#getSerialValue = conexArduino.read()
			#getSerialValue = conexArduino.read(6)
	pass

	def farent():
		global _a
		global t
		if _a == 1:
			faren = ((t * 1.8) + 32)
			boton.config(text=str(faren)+"ºf")
			_a = 0
		elif _a == 0:
			boton.config(text=str(t)+"ºc")
			_a = 1
			
	def stop():
		global s
		if s == True:
			s=False
			print s
		elif s == False:
			s= True
			print s

mainMedidor()