'''
<<<<<<< HEAD
#Modulo main.py
#! /usr/bin/env python

from clases import*

hola=Estacionamiento(1)
l=16
p="la3774"
m="toyota"
a=1999
c="rojo"
v=vehiculo(l,p,m,a,c)

l=12
p="lhola123"
m="corola"
a=122349
c="verde"
v1=vehiculo(l,p,m,a,c)

l=1
p="toma"
m="daka"
a=1999
c="teotisto es marico"
v2=vehiculo(l,p,m,a,c)

l=11
p="rata74"
m="ford"
a=1
c="azul"
v3=vehiculo(l,p,m,a,c)




hola.Estacionar(v)
hola.Estacionar(v1)
hola.Estacionar(v2)
hola.Estacionar(v3)



hola.mostrar()
=======
'''
#! /usr/bin/env python
# Programa de prueba

from tubo import *
from vehiculo import *
from estacionamiento import *
mi_carro1 = Vehiculo("carabobo4",5,"toyota",2008,"negro",1234)
mi_carro2 = Vehiculo("caracas1",3,"toyota",2010,"blanco",8456)
"""mi_carro3 = Vehiculo("valencia2",20,"ford",2012,"azul",123567)

mi_tubo1 = Tubo(15,"roro")
print(mi_tubo1.Cercano())
print(mi_tubo1.Retirar())
print(mi_tubo1.Estacionar(mi_carro1))
print(mi_tubo1.Estacionar(mi_carro2))
print(mi_tubo1.Estacionar(mi_carro3))
print(mi_tubo1.Cercano().modelo)
<<<<<<< HEAD
print(mi_tubo1.Existe("etiqueta",1234))
#>>>>>>> 2987ca18302ad99c4617001d1b36acbebb4fee89
=======
print(mi_tubo1.Existe("etiqueta",1234))"""

estacionamiento1 = Estacionamiento(1)
print(estacionamiento1.Estacionar(mi_carro1))
print(estacionamiento1.Estacionar(mi_carro2))
#print(estacionamiento1.Estacionar(mi_carro3))

print(estacionamiento1.ct[0].pv)
print(estacionamiento1.ct[1].pv)
print(len(estacionamiento1.ct[0].pv))
print(len(estacionamiento1.ct[1].pv))
"""print(estacionamiento1.ct[0].ocupacion)
print(estacionamiento1.ct[0].capacidad)
print(len(estacionamiento1.ct)) """
>>>>>>> 83ddc64eb2b1c4906c6ae1f5e5dfcefa6e690571