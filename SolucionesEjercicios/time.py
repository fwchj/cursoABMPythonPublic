# Ejercicio 1: mostrar la hora en la CDMX (version avanzada, ponder -6 para CDMX)
import time


# Preguntamos por la difrencia de horario
diff = input("What is the difference in hours with regard to UTC?\n(e.g. put -6 for Mexico City or 1 for Berlin)\n")

# Obtenemos la hora en EPOCH
timestamp = time.time()

# Calculamos las horas, minutas y segundos
seconds = timestamp  % 60;              # Usando el modulo obtenemos el numero de segundos desde el ultimo minuto
minutes = timestamp  / 60 % 60;         # Misma logica
hours = timestamp / (60 * 60) % 24;     # Misma logica

# Ajustamos el horario
hours += int(diff)

# En caso de no tener el mismo dia en UTC y el destino, tenemos que ajustar. 
if hours<0: 
    hours +=24
if hours>24: 
    hours -=24
 
# Imprimimos el resultado
print("La hora es %02.0f:%02.0f:%02.0f (Horario UTC %s)" % (hours,minutes,seconds,diff))

        