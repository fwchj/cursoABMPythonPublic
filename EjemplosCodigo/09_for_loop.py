#Ejemplo de un ciclo tipo 'for'

# Simple ciclo que va de 2 a 11 (range excluye el valor superior)
for i in range(2,12):
    print(i)
    
# Ejemplo con incrementos más complicados
print("------------------------------")
for x in (2**p for p in range(1, 7)):
    print(x)

# También podemos usar 'break' y 'continue' en estos ciclos    
print("------------------------------")
for i in range(1,11): 
    if i==5:
        continue
    if i == 8: 
        break;
    print(i)
    
