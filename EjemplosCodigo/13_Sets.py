# Ejemplo de como usar la estructura de datos tipo 'set'

# Definimos un SET
mi_set = {"Azul", "Rojo", "Verde"}

# El loop funciona igual como en list
for x in mi_set:
    print(x) 

# También podemos imprimir todo el set
print(mi_set)

# Agregamos y quitamos elementos
s = {"A","B","C"}
s.add("D")      # Agrega el valor D
s.remove("D")   # Quita el elemento D (manda error si no hay D)
s.discard("B")  # Quita el elemento B (NO manda error si no hay B)
s.pop()         # Quita el ultimo elemento (no sabemos cual es)
s.update(["X", "Y", "Z"]) # Agrega varios elementos

print(s)

# Podemos fácilmente comparar sets y juntar/combinar los sets
s1 = {"A","B","C"}
s2 = {"C","D","E"}

# Obtener la diferencia de los dos sets
print(s1.difference(s2))    # => A,B
# Obtener los elementos comunes de dos sets
print(s1.intersection(s2))  # => C
# Obtener indicador si no hay elementos en comun (True: no hay, False: sí hay)
print(s1.isdisjoint(s2))    # => False (ambos tienen C)
# Obtener indicador para ver si uno es un subset de otro
print(s1.issubset(s2))      # => False (s1 no es un subset de s2)
# Obtener indicador para ver si uno es un superset de otro
print(s1.issuperset(s2))    # => False (s1 is not a superset of s2)
# Hacer un set combinado sin los elementos comunes
print(s1.symmetric_difference(s2)) # A,B,D,E
# Generar un set que es la combinación de dos sets
print(s1.union(s2))         # => A,B,C,D,E


