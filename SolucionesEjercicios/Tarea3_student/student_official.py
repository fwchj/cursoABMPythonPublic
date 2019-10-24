# In this file we define the class 'Student' along with its methods
class Student: 
    def __init__(self,name,programme,year,female):
        self.name       = name
        self.programme  = programme
        self.generation = year
        self.female     = female
        self.grades     = []
    
    def addGrade(self,grade):
        self.grades.append(grade)
        
    def getGPA(self):
        csum = 0
        for i in self.grades:
            csum +=i
        return csum/len(self.grades)
    def getGender(self):
        if self.female==True:
            return "Woman"
        else: 
            return "Man"
        
    def describe(self):
        print("%-18s%-12s%-10s%-13s%4.2f" % (self.name,self.programme,self.getGender(),self.generation,self.getGPA()))


