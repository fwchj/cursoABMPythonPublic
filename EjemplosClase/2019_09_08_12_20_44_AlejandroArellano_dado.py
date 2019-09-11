# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 18:24:56 2019

@author: Alejandro Arellano Best
"""

"""
Importamos una función que nos permita generar número enteros de manera 
aletoria
"""
from random import randint
randint (1,6)
"""
le pedimos al usuario que esriba el número de veces que desea "lanzar el dado"
"""

print ("¿Cuantas veces quiere lanzar el dado?")
reps=int(input())

"""
hacemos el loop para que el dado sea lanzado el número de repeticiones.
Debemos nombrar una variable para las veces que el número sea par, y una para
impar
"""

par =0
impar=0
while reps != 0:
    dado=randint (1,6)
    if dado == 2 or dado ==4 or dado ==6:
        par+=1
        #print(dado, "par")
    else:
        impar+=1
        #print (dado,"impar")
    reps -=1
    
"""
Lo que sigue es reporta los datos. Para esto, importe una herramienta que me
permita graficar. Además, reportaré los resultados con palabas
"""

proporcion=(par, impar)
#from matplotlib import pyplot
#pyplot.pie(proporcion, labels=("par", "impar"))
#pyplot.show
print ("Los resultados del experimento fueron", par, "resultados par y", impar, "resultados impar.")
print ("Las proporciones fueron %2.2f por ciento par y %2.2f por ciento impar." %  (100*par/(impar+par), 100*impar/(impar+par)))










