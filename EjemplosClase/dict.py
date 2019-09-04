# Dictionnary

#Definimos el dictionario
mi_dict = {"A":4,"B":5,"b":99,"b":88}
print(mi_dict)
print(mi_dict["B"])
mi_dict["B"]=55
print(mi_dict)


# Loop sencillo (va sobre keys)
for i in mi_dict:
    print(i)
for i in mi_dict.values():
    print(i)

for i,j in mi_dict.items():
    print(i,"es",j)
    
print("profesor" in mi_dict)
print("B" in mi_dict)