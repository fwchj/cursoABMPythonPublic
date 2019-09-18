# Simplest possible example of OOP

# Defining the class
class Individual:
    # Constructor
    def __init__(self,salary,name,age,tenure,female):
        self.salary = salary
        self.name = name
        self.age = age
        self.tenure = tenure
        self.female = female
    
    # Method printing some basic information
    def describe(self):
        print("%s is %s years old, works since %s years in the company and earns a salary of %s\n" % (self.name,self.age,self.tenure,self.salary))    
  
vanessa = Individual(8729,"Vanessa",42,8,True)  
pedro   = Individual(5650,"Pedro",35,5,False)
i1      = Individual(4550,"Julia",28,0,True)


vanessa.describe()
pedro.describe()
i1.describe()




