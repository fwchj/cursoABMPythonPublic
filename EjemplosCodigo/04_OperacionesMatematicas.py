# Ejemplos de operaciones matemáticas básicas y avanzadas
# 1) Operaciones matemáticas básicas
# 2) Operaciones de asignacion compuesta
# 3) Operaciones matematicas mas avanzadas


# 1) Operaciones matemáticas básicas
a = 5   # Definimos una variable 'a' y ponemos el valor de 5
b = 10  # idem
c = 8   # idem
   
d = a + b; # suma:        d = 15
e = b - a; # resta:       e = 5
f = a * c; # producción:  f = 40
g = b / a; # división     g = 2
h = c % a; # modulus      h = 3

print(a,b,c,d,e,f,g,h,sep="\n")


# 2) Operaciones de asignacion compuesta
print("Compound assignment operators")
print("c=",c,", d=",d)
d **= c
print(d)


x = 2;        # x=2
x *= 2;       # x = x*2 = 4
x *= 2;       # x=8
x *= 2;       # x=16
x *= 2;       # x=32
print("x =",x)


# 3) Operaciones matematicas mas avanzadas
import math # Aqui importamos el paquete 'math'
print("\n\nOperaciones matematicas mas avanzadas:")
print("abs(-6.5)",abs(-6.5),sep=" = ")
print("math.ceil(-6.5)",math.ceil(-6.5),sep=" = ")
print("math.cos(5)",math.cos(5),sep=" = ")
print("math.exp(4)",math.exp(4),sep=" = ")
print("math.floor(6.5)",math.floor(6.5),sep=" = ")
print("math.log(55)",math.log(55),sep=" = ")
print("math.log10(55)",math.log10(55),sep=" = ")
print("max(4,44,9)",max(4,44,9),sep=" = ")
print("min(4,44,9)",min(4,44,9),sep=" = ")
print("math.sqrt(5.5)",math.sqrt(5.5),sep=" = ")
print("math.pow(4,5)",math.pow(4,5),sep=" = ")
