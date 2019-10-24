class Worker: 
    def __init__(self,name):
        self.name = name
        self.cumulativeNetIncome = 0
        self.incomeTaxPaid      = 0
        self.VATpaid = 0
        self.socialSecurityPaid = 0
    
    def describe(self):
        print("%-10.10s  %-15.15s %-10.2f %-10.2f %-10.2f %-10.2f" % (self.name,self.getType(),self.incomeTaxPaid,self.VATpaid,self.socialSecurityPaid,self.cumulativeNetIncome));

    def getType(self):
        if type(self) is Owner:
            return "Owner"
        elif type(self) is Contractor:
            return "Contractor"
        elif type(self) is Employee:
            return "Employee"
        else: 
            return "Unknown type"

# OWNER ---------------
class Owner(Worker):
    def __init__(self,name):
        Worker.__init__(self,name)
    
    def payWage(self,profit):
        grossIncome = max(0,min(0.8*profit, 150000))
        VAT = 0
        incTax = 0.2*grossIncome
        socialSecurity = 0.1*grossIncome
        
        # Store the cumulative values for the individual
        self.cumulativeNetIncome    +=0.7*grossIncome
        self.incomeTaxPaid          += incTax
        self.VATpaid                += VAT
        self.socialSecurityPaid     +=socialSecurity
        
        result = {"socialSecurity":socialSecurity,"incomeTax":incTax,"vat":VAT,"netIncome":0.7*grossIncome}
        print("Payment to owner: gross: %s, net: %s\n" % (grossIncome,0.7*grossIncome))
        return result

# Contractor
class Contractor(Worker):
    def __init__(self,name,grossIncome):
        self.grossIncome = grossIncome
        Worker.__init__(self, name)

    def payWage(self):
        VAT = 0.16*self.grossIncome
        incTax = 0.1*self.grossIncome
        
        #Store the cumulative values for the individual
        self.cumulativeNetIncome    += 0.9*self.grossIncome
        self.incomeTaxPaid          += incTax
        self.VATpaid                += VAT
        
        
        result = {"socialSecurity":0.0,"incomeTax":incTax,"vat":VAT,"netIncome":0.9*self.grossIncome}
        return result;
    
# Normal employee
class Employee(Worker):
    def __init__(self,name,grossIncome):
        self.grossIncome = grossIncome  
        Worker.__init__(self, name)
    
    def payWage(self):
        VAT = 0;
        incTax = 0.2*self.grossIncome;
        socialSecurity = 0.1*self.grossIncome;
        
        # Store the cumulative values for the individual
        self.cumulativeNetIncome+=0.7*self.grossIncome
        self.incomeTaxPaid    += incTax
        self.VATpaid        += VAT
        self.socialSecurityPaid +=socialSecurity
        
        result = {"socialSecurity":socialSecurity,"incomeTax":incTax,"vat":VAT,"netIncome":0.7*self.grossIncome}
        return result;  
        
        
        
