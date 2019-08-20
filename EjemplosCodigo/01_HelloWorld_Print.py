# Ejemplo inicial para mostrar como se imprime información en 
# la consola. 

#En la siguiente linea imprimimos algo en la consola
print("Hello World!")


#Combinamos varios valores
print("Hello, my age is",25,"years")
# imprime: Hello, my age is 25 years
print("Hello, my age is",25,"years",sep="--")
# imprime: Hello, my age is--25--years

print("El costo del producto %05.0f es %6.2f" % (4,33.12345))
#imprime: El costo del producto 00004 es  33.12

print("A = %s" % 12345.123456789)     # A = 12345.123456789
print("A = %.6f" % 12345.123456789)   # A = 12345.123457
print("A = %.0f" % 12345.123456789)   # A = 12345
print("A = %3.5f" % 12345.123456789)  # A = 12345.12346
print("A = %15.5f" % 12345.123456789) # A =     12345.12346
print("B = %s" % 4)                   # B = 4     
print("B = %3.2f" % 4)                # B = 4.00
print("B = %03.2f" % 4)               # B = 4.00
print("B = %05.2f" % 4)               # B = 04.00
print("B = %05d" % 4)                 # B = 00004
print("C = %5.3g" % 1234.123456789)   # C = 1.23e+03
print("C = %5.3g" % 12.123456789)     # C = C =  12.1
print("D = %05.2f" % 1.2334)          # D = 01.23
print("-------------------------------")

# Con \n podemo hacer una nueva línea y con \t un tab
print("Hola, me llamo Juan\ny vivo en\t\t México\'")
"""
Imprime: 
Hola, me llamo Juan
y vivo en         México
"""
print("\n\n\n") # Imprime 3 líneas vacías


# Ejemplo completo 
print("-----------------\nNombre\t%6s\nPrecio\t%6.2f\nCodigo:\t%06d\nQty:\t%6d" % ("Leche",3,13.1,37))
