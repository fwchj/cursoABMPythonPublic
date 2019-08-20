# Ejemplo de como manejar excepciones (Exception handling)

# Definimos una lista
a = [1,2]

try: 
    print(a[2]) #Tratamos de imprimir un indice que no existe!
except IndexError:
    print("The requested index is not available. The highest available index is %s" % (len(a)-1))
except:
    print("An unknown error occured")
finally: 
    print("The full array is: ",a)
    
    

print("============================================")

try: 
    year_of_birth = int(input("What is your year of birth?\n"))
    age = 2019 - year_of_birth
    print("You turn %s years this year" % age)
except ValueError:
    print("ERROR: it seems that you did not enter a numerical value")
    print("I abort")
    



