class Firm():
    def __init__(self,capital):
        self.capital    = capital
        self.paidPersonalIncome = 0
        self.paidVAT = 0.0
        self.paidCorporateIncomeTax=0
        self.paidSocialSecurity = 0

        self.employees = []
        self.owner = "";
        
    def menu(self):
        option =0;
        while option!=3 :
            print("Main menu\n==========================");
            print("1: Pay salaries");
            print("2: Display current state");
            print("3: Exit program");
            
            
            option = int(input())
            if option==1:
                self.paySalaries()
            elif option==2:
                self.displayState()
            elif option==3: 
                print("Thank you for using this software. See you soon!")
            else:
                print("ERROR: Unrecognised option, please try again!")
            
    def displayState(self):
        print("The current state of the firm is the following:")
        print("Capital                 %9.2f" % self.capital)
        print("Paid social security    %9.2f" % self.paidSocialSecurity)
        print("Paid income tax         %9.2f" % self.paidPersonalIncome)
        print("Paid corporate tax      %9.2f" % self.paidCorporateIncomeTax)
        print("Paid value added tax    %9.2f" % self.paidVAT)
        
        print("\nStatistics of each employee of the firm:")
        print("%-10.10s  %-15.15s %-10.10s %-10.10s %-10.10s %-10.10s" % ("Name","Contract","Income tax","VAT paid","SS paid","Net income"))
        self.owner.describe()
        for w in self.employees:
            w.describe()
        
        print("\n");
    def paySalaries(self):
        print("Please indicate the profit before paying salaries:")
        profit = float(input())
        
        # Pay to all employees
        for w in self.employees: 
            result = w.payWage();
            
            
            self.paidSocialSecurity        +=result["socialSecurity"]
            self.paidPersonalIncome        +=result["incomeTax"]
            self.paidVAT                   +=result["vat"]
            paymentTotal = result["socialSecurity"]+result["incomeTax"]+result["vat"]+result["netIncome"];
            profit -=paymentTotal;
            
        
        
        # Now we can pay corporate taxes
        if profit>0 :
            self.paidCorporateIncomeTax +=0.3*profit;
            profit = 0.7*profit;
        
        ## Pay the owner
        result = self.owner.payWage(profit);
        self.paidSocialSecurity        +=result["socialSecurity"];
        self.paidPersonalIncome        +=result["incomeTax"];
        self.paidVAT                +=result["vat"];
        paymentTotal = result["socialSecurity"]+result["incomeTax"]+result["vat"]+result["netIncome"];
        profit -=paymentTotal;
        
        
        
        # Adapt the capital
        self.capital+=profit;
        
        
    
