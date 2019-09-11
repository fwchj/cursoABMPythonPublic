#Autor:Yarim Alberto Vargas Flores
import random
f=0
t=0
y=0
u=0
g=0
x=0
i=1
d=0
r=0
print("¿Cuantas veces quieres tirar el dado?")#Le pide al usuario cuantas veces quiere tirar el dado.
g=int(input())#guarda en una variable el numero de veces que se va a tirar el dado.
h=[]#declaras la lista que va a guardar los numeros que salen en el dado.
for i in range(0,g) :#ciclo para tirar repetidas veces el dado.
   u= random.randint(1,6)#genera un numero aleatorio del 1 al 6.
   y+=u#variable que guarda la suma de los numeros que salen en el dado (no estoy seguro de que esto sea necesario aun asi lo puse).
   h.append(u)#guarda los numeros que salen en el dado en una lista h
   z=h[x]#guarda en una variable la entrada x de h
   x+=1#contador para sincronizar las posiciones de h.
   if (z%2==0):#revisa si el numero z tiene modulo 0 con 2.
       t+=1 #contador para numeros pares
   else: f+=1#contador para numeros impares.
d=(t*100)/g
r=(f*100)/g
print("se obtuvieron los siguientes numeros en el lanzamiento del dado",h)
print("la suma de los numeros obtenidos en el dado son",y)
print("la cantidad de numeros pares es",t,"y de impares",f)
print("el porcentaje de numeros pares es", d, "y el de numeros impares es",r)
input('Press ENTER to exit') 