# OOP with inheritance

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

# Defining the sub-class (inherited from Individual) 
class Owner(Individual):
    def __init__(self,salary,name,age,tenure,female,shares):
        self.shares = shares
        Individual.__init__(self,salary, name, age, tenure, female)
         
    def describe(self):
        print("%s is %s years old, owns the company since %s years and earns a salary of %s. She has %s shares of the company\n" % (self.name,self.age,self.tenure,self.salary,self.shares))    

     
vanessa = Owner(8729,"Vanessa",42,8,True,100)
pedro   = Individual(5650,"Pedro",35,5,False)

vanessa.describe()
pedro.describe()




