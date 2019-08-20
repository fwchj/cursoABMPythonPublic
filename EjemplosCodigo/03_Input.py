# Example on how to read input from the console (e.g. ask the user for an input)
print("Favor de ingresar un primer número")
a = float(input()) #usamos float() para convertir todo a float
print("Gracias, favor de ingresar un segundo número")
b = float(input())
print("La suma de %s y %s es %s" % (a,b,a+b))  