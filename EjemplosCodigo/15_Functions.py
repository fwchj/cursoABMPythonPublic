# Ejemplos de como usar las funciones

# Very simple example: adding two numbers
def suma(x1,x2):
    return x1 + x2
print(suma(1,3))

def prueba():
    print("Hola, soy una función que se llama prueba()")
prueba()


# Default parameters
def hola(name="amigo"):
    print("Hola %s" % name)
hola()           # Imprime: Hola amigo
hola("Juan")     # Imprime: Hola Juan


# Parametros son locales
print("--- Ejemplo de parámetros locales ---")
def resta(x1,x2):
    return x1-x2
x1 = 2
x2 = 3
print(x1,x2)
print(resta(44,4))
print(x1,x2)


# Function with endogenous number of arguments
def math(operation,*argv):
    if(operation=="sum"):
        suma = 0
        for i in argv:
            suma +=i
        print("Sum of ",argv," is ",suma)
    else:
        product = 1
        for i in argv:
            product *=i
        print("Product of ",argv)

math("sum",1,2,3)
math("sum",1,2,3,4)
math("product",1,2,3,4,5)

  
# Function with endogenous key-value-pairs  
def gen_dict(**kwargs): 
    for k,v in kwargs.items():
        print("%s\t=>  %s" % (k,v)) 
        
gen_dict(name="Jessica",age="34",height="178cm")



# Pass-by-reference illustration
def square_list(lista):
    for i in range(0,len(lista)):
        lista[i] = lista[i]**2
    print(lista)
a = [1,2,3]
square_list(a) # => [1, 4, 9]
print(a)       # => [1, 4, 9]

# Pass-by-value (for primitive types)
def square_value(x1):
    x1 = x1**2
    print("The square is ",x1)
x1 = 2
square_value(x1) # => The square is 4
print(x1)        # => 2


# Recursive functions
def sum_of_halfs(start,precision):
    if start>=precision:
        result = start/2+sum_of_halfs(start/2,precision)
    else:
        result = 0
    
    return result
print(sum_of_halfs(6,0.000001))
print(sum_of_halfs(6,0.1))


# Function with multiple values as return
def suma_resta(x1,x2): 
    return x1+x2,x1-x2
suma,resta = suma_resta(66,34)
print(suma,resta)