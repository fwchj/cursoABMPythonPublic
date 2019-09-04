# Ejemplos de list

mi_lista = [1,2,3,4]
print(mi_lista)
print(type(mi_lista))

# Imprimir un elemento en particular (tercero)
print(mi_lista[2])
print(type(mi_lista[2]))

# Agregar un 2.5 entre el 2 y el 3
mi_lista.insert(2,2.5)
print(mi_lista)
print(mi_lista[2])

print("El tamanio es: %s" % len(mi_lista))

# Eliminamos todos los elementos
mi_lista.clear()
print(mi_lista)


print("Ilustracion de pointers-------")

a = [1,3,5,7,9]
b = a 
c = a.copy()
a[4]=-4
print(a)
print(b)
print(c)

m = [[1,2],[3,[4,"Hola"]]]
print(m)
print(m[1][1][1])

print("______________________________")


v = [2,4,5,3,6,7,9]
suma = 0
for u in v:
    suma +=u
    print(u,suma)
    
print("la suma es ",suma, "y el promedio es",  suma/len(v))





























