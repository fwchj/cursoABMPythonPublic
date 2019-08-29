"""
Este ejemplo de clase calcula la serie 1/(x^a) para a={1,2,3,...} hasta llegar 
a un valor menor a 0.00001 o bien llegar a 100 iteraciones
"""

# Parametros
maxiter = 100

# Variables secundarias
a       = 1
iter    = 0

# Pedir el valor de x al usuario
print("Favor de indicar el valor x:")
x = float(input())

# Calculo inicial
result  = 1 / (x**a)

# Ciclo while porque no sabemos cuantas iteraciones necesitamos
while(result >= 0.00001): 
    result = 1 / (x**a)         # Calculo el nuevo resultado
    print(iter,result,sep=": ") # Imrimo el resultado
    a +=1                       # Incremento a por una unidad
    iter +=1                    # Incremento el contador de iteraciones        
    if iter>maxiter:            # Verifico si no llegamos al máximo de iteraciones
        print("Termino porque llegué al máximo de iteración")
        break
