
class Animal:
    def __init__(self,nombre,duracion_de_vida,peso,ecosistema):
        self.nombre= nombre
        self.duracion_de_vida = duracion_de_vida
        self.peso = peso
        self.ecosistema = ecosistema
        print("Creamos un animal")
        
    def describe(self):
        print("Soy un animal del tipo %s" % self.nombre)
        

class Reptiles(Animal):
    def __init__(self,nombre,duracion_de_vida,peso,ecosistema,numero_de_huevos):
        self.numero_de_huevos = numero_de_huevos
        Animal.__init__(self, nombre,duracion_de_vida, peso, ecosistema)
        print("Creamos un Reptil")
    def describe(self):
        print("Soy un reptil de tipo %s" % self.nombre)
        
        
# Usamo las clases
serpiente = Reptiles("Serpiente",15,25,"selva",2)
print("---------")
hormiga = Animal("Hormiga",2,0.001,"en mi casa")

print(type(serpiente))
print(type(hormiga))

serpiente.describe()

