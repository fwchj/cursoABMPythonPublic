# Este archivo muestra alungas de las opciones del paquete 'random'

import random as rd

# Seleccionar un elmento aleatorio de una lista/tuple o similar
miLista = [1,5,7,8,4]
print(rd.choice(miLista)) 
print(rd.choice(miLista)) 
print(rd.choice(miLista)) 


# Enteros aleatorios con distribucion uniforme
print("------")
print(rd.randint(0,25))
print(rd.randint(0,25))
print(rd.randint(0,25))

# Float aleatorios con distribucion uniforme entre 0 y 25
print("------")
print(rd.random()*25)
print(rd.random()*25)
print(rd.random()*25)

# Distribucion normal con promedio 5 y sd=3
print("------")
print(rd.gauss(5,3))

# Shuffle de una lista (o similar)
print("------")
print(miLista)
rd.shuffle(miLista)
print(miLista)
rd.shuffle(miLista)
print(miLista)
