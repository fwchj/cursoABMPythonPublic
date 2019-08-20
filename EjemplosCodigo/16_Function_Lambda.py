# Ejemplo para ilustrar las funciones lambda

# Definimos una función muy sencilla y la usamos
square = lambda a: a**2
print(square(4)) # => 16


# Ahora mostramos la utilidad del uso de funciones lambda
def power(x):   #definimos una funcion normal
    return lambda a : a**x  # en la funcion, usamos una funcion lambda

power2 = power(2)   # aqui generamos unas funciones similares
power3 = power(3)

print(power2(5))    #aquí ya podemos usar las funciones similares
print(power3(5))