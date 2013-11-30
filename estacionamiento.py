#! /usr/bin/env python
# Modulo Estacionamiento
from random import *
from tubo import *
class Estacionamiento(object):

	etiqueta = 0
	ct = []
	ticket_tubo = 0
	ticket_vehiculo = 0
	tamanyo_estacionamiento = 0


	def __init__(self,e):
		self.etiqueta = e


	def Generar(self):	 
		nuevo_tubo = Tubo(randint(5,25), self.ticket_tubo)
		self.ticket_tubo += 1
		self.tamanyo_estacionamiento += 1 
		self.ct.append(nuevo_tubo)

	def Pop(self,*arg):
		self.ticket_tubo -= 1
		self.tamanyo_estacionamiento -= 1
		if len(arg) == 1:
			self.ct.pop(arg)
		else:
			self.ct.pop()


	def Estacionar(self,vehiculo):
		if self.tamanyo_estacionamiento == 0:
			self.Generar()
			while self.ct[0].capacidad < vehiculo.longitud:
				self.Pop(0)
				self.Generar()
			self.ct[0].Estacionar_tubo(vehiculo)
			tubo_estacionar = self.ct[0].etiqueta


		else:
			i = 0
			hay_espacio = False
			while (( i < self.tamanyo_estacionamiento) and not(hay_espacio)):

				if (self.ct[i].capacidad - self.ct[i].ocupacion) >= vehiculo.longitud:
					self.ct[i].Estacionar_tubo(vehiculo)
					tubo_estacionar = self.ct[i].etiqueta
					hay_espacio = True
					break
				else: 
					i += 1

<<<<<<< HEAD
		if not(hay_espacio):
			self.Generar()
			self.ct[i].Estacionar(vehiculo,self.ticket_vehiculo + 1)
=======
			if not(hay_espacio):
				self.Generar()
				while self.ct[len(self.ct) - 1].capacidad < vehiculo.longitud:
					self.Pop()
					self.Generar()

				self.ct[len(self.ct) - 1].Estacionar_tubo(vehiculo)
				tubo_estacionar = self.ct[len(self.ct) - 1].etiqueta
>>>>>>> 83ddc64eb2b1c4906c6ae1f5e5dfcefa6e690571

		self.ticket_vehiculo += 1
		return tubo_estacionar 



	def Existe(self,placa,ticket,*arg):

		i = 0
		existe=False
		while  i < self.tamanyo_estacionamiento and not(existe):
		     j = 0
		     while j < len(self.ct[i].pv) and not(existe):

		     		if self.ct[i].pv[j].Existe("placa",placa) and self.ct[i].etiqueta == ticket:
		     			existe=True
		     		else:
		     			j += 1
		     i += 1
		
		if len(arg)==2 and existe: 
		 	arg[0]=i-1
		 	arg[1]=j
		 
		 
		return existe

	
	def Retirar(self,placa,ticket):

		j=0
		
		if self.Existe(placa,ticket):
			for i in range(0,len(self.ct)):
				tubo_explota = False
				while not len(self.ct[i].pv) == 0 and self.ct[i].etiqueta == tickect:
					tubo_explota = True
					vehiculo = self.ct[i].Retirar() 
					if placa == vehiculo.placa and j == 0:
						tubo = self.ct[i].pv
						return "El vehiculo se ha retirado correctamente"
						break
					else:
						if placa == vehiculo.placa:
							return "El vehiculo se ha retirado correctamente"
						else:
							tubo = Tubo(self.ct[i].capacidad, self.ct[i].etiqueta)
							tubo.Estacionar(vehiculo)
					j += 1
			
				if tubo_explota:
					self.ct.pop(i)
					self.ct.append(tubo)						
					break	
		
		else: 
			return "No existe un vehiculo con esos atributos"
			


	def Destruir(self):
	
		self.tamanyo = self.tamanyo - 1
		self.ct.pop(1)

	def Vaciar(self,etiqueta):
		i=0
		existe=False
		while (i < len(self.ct)) and not(existe):
			if self.ct[i].etiqueta == etiqueta:
				existe = True
			else: 
				i=i+1

		if existe:
			print(i)
			for j in range(len(self.ct[i].pv)):
				vehiculo=self.ct[i].Cercano()
				self.ct[i].Retirar()
				self.Estacionar(vehiculo,i)
			self.ct.pop(i)	
				
			return "Se Vacio el tubo"

		else:
			return "No existe un tubo con esta etiqueta"

