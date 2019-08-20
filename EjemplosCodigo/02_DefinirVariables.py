# En este archivo mostrarmos como se definen variables
x = 5             # Definimos una variable del tipo 'int'
print(type(x),x)
y = 5.5           # Definimos una variable del tipo 'float'
print(type(y),y)
z = True
print(type(z),z)  # Definimos una variable del tipo 'bool'
s = "Hello"
print(type(s),s)  # Definimos una variable del tipo 'str'

x = x / 2         # El tipo se ajusta automáticamente, aquí  'int' -> 'float'
print(type(x),x)
