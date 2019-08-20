import csv

with open('employee_file.txt', mode='w',newline='') as employee_file:
    employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    employee_writer.writerow(['Name', 'Area', 'Tenure'])

    employee_writer.writerow(['John Smith', 'Accounting', 5])
    employee_writer.writerow(['Erica Meyers', 'IT', 2])
    

# Any type of information (not csv)
with open('random_text.txt',mode='w') as myfile:
    myfile.write("Hello\n")
    myfile.write("World!")
    myfile.write("\n\tThe value is %.3f" % 123.456789)
    
    