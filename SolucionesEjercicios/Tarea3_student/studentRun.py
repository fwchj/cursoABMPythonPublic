from student import Student


# Create the students and add some grades
laura = Student("Laura","ME",2008,True)
laura.addGrade(9.5)
laura.addGrade(8.5)

stephan = Student("Stephan","UM",2016,False)
stephan.addGrade(10.0)
stephan.addGrade(8.5)

john = Student("John","MAPP",2012,False)
john.addGrade(6.7)
john.addGrade(8.2)


# Print data
print("%-18s%-12s%-10s%-13s%3s" % ("Name","Programme","Gender","Generation","GPA"))
print("-------------------------------------------------------------")
laura.describe()
stephan.describe()
john.describe()