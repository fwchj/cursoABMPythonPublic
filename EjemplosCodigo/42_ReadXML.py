#Read a XML file

#import the required package
import xml.etree.ElementTree

# Load the file
file = xml.etree.ElementTree.parse("workers.xml").getroot()

# Loop over all "Employee"
for employee in file.findall("Employee"):
    #Get the data (get for attributes), find for tags
    type        = employee.get("type")             # get attribute
    name        = employee.find("Name").text
    familyname  = employee.find("FamilyName").text
    female      = employee.find("Female").text 
    age         = employee.find("Age").text
    salary      = employee.find("GrossSalary").text 
    
    # Print the information
    print(type,name,familyname,female,age,salary,sep="|")
    print(female)
   
    
    