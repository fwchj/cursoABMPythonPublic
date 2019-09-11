
# Autor: Alejandro Alberto Miliano


import random                                        # Importamos el paquete "random" para generar números aleatorios con igual probabilidad de ocurrencia
n=int(input("Cuántas veces desea lanzar el dado:"))  #La variable "n" pregunta y captura el número de lanzamientos. Aquí el usuario introduce un número.
p=0                                                  # Con la variable "p" inciamos el contador para los números pares
for i in range(1,n+1):                               # corremos el ciclo for de 1 a n+1, agregamos 1 a la frontera superior para que el conteo llegue hasta n.
    s=randint(1,6)                                   # generamos un número aleatorio entre 1 y 6,incluyendo los extremos, y con igual probabilidad de ocurrencia
    if s%2==0:                                       #Para cada resultado del lanzamiento,examinamos si es par o impar usando el residuo. Si es par el residuo de dividir entre 2 debe ser cero.
          p=p+1                                      # Si la condición lógica se cumple el contador se incrementa en una unidad.
          print("El resultado del lanzamiento #",i,"fue:",s,"y es par")    # Si la condición lógica se cumple significa que el resultado fue par
    else:
         print("El resultado del lanzamiento #",i,"fue:",s,"y es impar")   # Si la condición lógica no se cumple entonces se trata de un número impar

print("------------------ESTADÍSTICA DESCRIPTIVA---------------------\nCantidad de números pares:\t%6d\tPorcentaje:\t%6.2f\nCantidad de números impares:\t%6d\tPorcentaje:\t%6.2f" %(p,(p/n)*100,n-p,((n-p)/n)*100))
# En esta última línea de código, imprimimos las estadísticas descriptivas solicitadas, haciendo uso del salto de línea y espacios entre las cantidades. Me basé en lámina 36 vista en clase.
