# Import required packages
import json

# Open the file and load json into 'data'
with open("workers.json",'r') as f:
    data = json.load(f)
   
# We see the json is imported as dictionnary 
print(type(data))

# Get the element 'Employee'
employees = data["Employee"]
print(type(employees))
for e in employees: # loop through all employees
    print(e) #again, we have a dictionnary

# Get element CompanyName and print it
company = data["CompanyName"]
print(company)