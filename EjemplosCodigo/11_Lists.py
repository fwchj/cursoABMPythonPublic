# Ejemplo de la estructura de datos tipo 'list'

# Definir una lista con 10 elementos
c = [9.5,8.7,6.5,10]
print(c)

# Obtener un elemento en particular (aqui el penultimo y el ultimo): 
print(c[2],type(c[2]))
print(c[3],type(c[3]))

#tambien ponemos contar desde atras: 
print(c[-1],type(c[-1]))

# Agregar un elemento (al final)
c.append(9.8)
print(c)

#Agregar un elemento en una posicion particular
print("Indice 2 antes:",c[2])
c.insert(1,2.5)
print("Indice 2 despues:",c[2])
print(c) # Los elementos a la derecha se mueven a un indice mayor


# Cambiar un elemento en particular
c[1] = 8.8
print(c,"Después del cambio de c[1]")

# Eliminar un elento particular (aqui el indice 1) 
c.pop(1)
print(c)

# Obtener el tamanio de la lista
print("La lista tiene %s elementos" % len(c))

# Eliminar todos los elementos de una lista (sin borrar el objeto)
c.clear()
print(c)


# OJO: lists son punteros! 
x = [1,2,3,4]
y = x 
z = x.copy()
x[0] = 5
print(y)
print(z)


print("-------")
x = [1,2,3,4] # x=[1,2,3,4]
y = x         #copy x to y=> y=[1,2,3,4]

x[3]=99     # change the last value of x => x=[1,2,3,99]
            # HOWEVER: now y is also y=[1,2,3,99]
print(y)


print("----- La manera correcta de hacerlo -----")
x = [1,2,3,4]

y = x.copy()
 
x[3]=99     # change the last value of x => x=[1,2,3,99]
# we have: x=[1,2,3,99] and y=[1,2,3,4]        
print(x,y)


## MULTIDIMENSIONAL LISTS

x = [[1,2,3,4],[5,6,7,8,0]]
print(x)
print(x[0][3])


# FOR LOOP THROUGH INDEXES
print("Loops (version 1):")
x = [1,2,3,4,5,6,7]
for i in range(0,len(x)):
    print(x[i])

print("Loops (version 2):")
for i in x:
    print(i)
