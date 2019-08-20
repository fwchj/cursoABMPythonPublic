# OOP with inheritance

# Defining the classes
class Firm: 
    def __init__(self,name,profit,cash):
        self.name=name
        self.profit = profit
        self.cash = cash
        self.workers = []
        
    def addWorker(self,*argv):
        for w in argv:
            self.workers.append(w)
        
    def listAllWorkers(self,minTenure=0):
        print("------- LIST OF EMPLOYEES: -----")
        for w in [x for x in self.workers if x.tenure >=minTenure]:
            w.describe()
        print("--------------------------------")
 
      
        
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
        print("%s is %s years old, works since %s years in the company and earns a salary of %s" % (self.name,self.age,self.tenure,self.salary))    
 
class Owner(Individual):
    def __init__(self,salary,name,age,tenure,female,shares):
        self.shares = shares
        Individual.__init__(self,salary, name, age, tenure, female)
         
    def describe(self):
        print("%s is %s years old, owns the company since %s years and earns a salary of %s. She has %s shares of the company" % (self.name,self.age,self.tenure,self.salary,self.shares))    

class Director(Individual):
    def __init__(self,salary,name,age,tenure,female,boss):
        self.boss = boss
        self.subordinates = []
        Individual.__init__(self,salary, name, age, tenure, female)
    def add_subordinate(self,worker):
        self.subordinates.append(worker)
        
class Clerk(Individual):
    def __init__(self,salary,name,age,tenure,female,boss,task):
        self.boss = boss
        self.task = task
        Individual.__init__(self,salary, name, age, tenure, female)

   


# Aqui iniciamos a usar los objetos

# Generamos 3 objetos de Individual (de diferentes tipos)   
vanessa = Owner(8729,"Vanessa",42,8,True,100)
pedro   = Director(5650,"Pedro",35,5,False,vanessa)
juan    = Clerk(3500,"Juan",28,2,False,pedro,"Invoicing")
# Generamos una empresa
myFirm  = Firm("Mi empresa",0,10000)
# Agregamos las personas a la empresa
myFirm.addWorker(vanessa,pedro,juan)
print(myFirm.workers)

# Solicitamos la lista de trabajadores
myFirm.listAllWorkers()     # complete list
myFirm.listAllWorkers(5)    # list of employees with tenure >=5



