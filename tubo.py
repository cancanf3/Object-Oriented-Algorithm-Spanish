#! /usr/bin/env python
# Modulo de Tubo
from vehiculo import *
class Tubo(object):
	capacidad = 0
	ocupacion = 0
	etiqueta = 0
	pv = []

	def __init__(self,tamanyo,e):
		self.capacidad = tamanyo
		self.etiqueta = e


	def Cabe(self,vehiculo):
		if (vehiculo.longitud) <= (self.capacidad - self.ocupacion):
			return True
		else:
			return False


	def Existe(self,atributo,valor):
		existe = False	
		for i in self.pv:
			if ( atributo == "longitud") and ( i.longitud == valor):
				existe = True
			elif ( atributo == "placa") and ( i.placa == valor):
				existe = True
			elif ( atributo == "modelo") and ( i.modelo == valor):
				existe = True
			elif ( atributo == "anyo") and ( i.anyo == valor):
				existe = True					
			elif ( atributo == "color") and ( i.color == valor):
				existe = True
			elif ( atributo == "etiqueta") and ( i.etiqueta == valor):
				existe = True
			if existe == True: 
				break	
		return existe
	

	def Estacionar_tubo(self,vehiculo):	
		if self.Cabe(vehiculo):
			self.ocupacion += vehiculo.longitud
			self.pv.insert(0,vehiculo)
			return "El vehiculo se ha estacionado correctamente"

		else:
			return "El tubo no tiene capacidad para estacionar este vehiculo"


	def Retirar(self):
		if self.ocupacion == 0:
			return "El tubo esta vacio"

		else: 
			self.ocupacion -= self.pv[0].longitud
			return self.pv.pop(0)


	def Cercano(self):
		if self.ocupacion > 0:
			return self.pv[0]

		else:
			return "No hay vehiculos en el tubo"
