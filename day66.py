'''
INSTANCE VARIABLE:
if there is any instance varibale in class then it will show, if not then it will show class var

'''
class employee:
    CompanyName="Apple"   #class variable, related to class(same for everyone,common)
    def __init__(self,name):
        self.name=name
        self.raise_amount=0.2    #instance variable(might be different for everyone)
    def showdetails(self):
        print(f"The name of the employee is {self.name} and the raise amount in {self.CompanyName} is {self.raise_amount}")

a=employee("Soniya")
a.raise_amount=0.3    #instance variable
a.CompanyName="Apple India"    #instance variable
a.showdetails() 
b=employee("Sanjay")
b.showdetails()


