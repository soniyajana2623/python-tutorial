# SETTERS-->set value of instance variables
# GETTERS-->get value of instance variable
class employee:
    def setname(self,nm): # to set the value
        self.name=nm
    def getname(self):  #to get the value
        print("The name is:", self.name) 

e1= employee()
e2= employee()
e3=employee()

e1.setname(input("Enter your name:"))
e2.setname(input("Enter your name:"))
e3.setname(input("Enter your name:"))

print("Employee 1:\n", e1.__dict__)
print("Employee 2:\n", e2.__dict__)
print("Employee 3:a\n", e3.__dict__)

e1.getname()
e2.getname()
e3.getname()
