# Ejemplo de operadores lógicos

# Definimos unas variables que usaremos después:
age                 = 66
female              = True
numberOfSeniorWomen = 0
weekEnd             = True
officialHoliday     = False

#Ejemplo 1: doble condición de tipo 'and'
if age>65 and female==True : 
    numberOfSeniorWomen+=1;  
    #is executed only for women with age above 65 years
print(numberOfSeniorWomen) 

 
# Ejemplo 2: doble condición de tipo 'or'
        
if weekEnd==True or  officialHoliday==True: 
    # The following message will be displayed on days of the weekend and during official holidays.
    print("Sorry, we are closed today!")  

# Ejemplo 3: puede importar el órden de las condiciones. 
i = 1 #Ver que pasa si ponemos i=0
if i!=0 and 10/i>5: 
    print("test1")
    
if 10/i>5 and i!=0 :
    print("test2")

