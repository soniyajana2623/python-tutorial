class Employee:
    def __init__(self,name, emip,edu):
        self.name= name
        self.emip= emip
        self.edu= edu

    def showDetails(self):
        print(f"The name of Employee {self.emip} is {self.name}") 

class Managers(Employee):
    def show(self):
        print("Welcome")


e1= Employee("Soniya",2623,"Bcom")
e1.showDetails()
e2= Managers("Sanjay",2435,"BTech")
e2.showDetails()
e2.show()



