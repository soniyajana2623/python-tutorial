'''
Single Inheritance:
'''

class Students:
    def __init__(self,name,roll_no):
        self.name= name
        self.roll_no= roll_no
    def showDetails(self):
        print(f"The name of the student is {self.name} and his/her roll no. is {self.roll_no}")
    
class Div_A(Students):
    def marks(self,marks):
        self.marks= marks
    def showDetails1(self):
        print(f"He/she scored {self.marks}")
        
    
s1=Div_A("Soniya",26)
s1.showDetails()
s1.marks(80)
s1.showDetails1()



class Animal:
    def __init__(self,name,colour):
        self.name = name
        self.colour = colour
    def show(self):
        print(f"I have a cat name {self.name} and his colour is {self.colour}")

class cat(Animal):
    def __init__(self,name,age):
        Animal.__init__(self,name,colour="orange")
        self.age= age
    def show(self):
        print(f"He is {self.age} years old")

a=Animal("sanjay","orange")
a.show()

c=cat("sanjay",1)
c.show()








