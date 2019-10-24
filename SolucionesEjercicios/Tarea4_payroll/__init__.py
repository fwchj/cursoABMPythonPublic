from firm import Firm
from workers import *

myfirm = Firm(1000000.00)
myfirm.employees.append(Employee("John", 80000))
myfirm.employees.append(Employee("Jane", 85000))

myfirm.employees.append(Contractor("Peter", 67000))
myfirm.employees.append(Contractor("Paula", 52000))

myfirm.owner = Owner("Nancy")

myfirm.menu()