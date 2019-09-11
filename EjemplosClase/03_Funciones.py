
def prueba():
    print("hola mundo")

def resta(a,b):
    print(a-b)
    return a-b
    
r = resta(23,4)


# Ejemplo con valor default

def power(x,a=2):
    return x**a

print(power(10))
print(power(2,a=3))


# **kwargs
print("______________________________________-")
def dict(**kwargs):
    print(kwargs)
    print(type(kwargs))
    print(type(kwargs["c"]))
    
dict(a="5",b=6,c=True)

print("-------------------------------------------------")

def printNumber(start):
    print(start)
    start +=1
    printNumber(start)

printNumber(1)















