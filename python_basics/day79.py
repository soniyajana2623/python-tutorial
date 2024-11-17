'''
Multiple Inheritance:
Can have multiple parent class 
'''

class div_A:
    def __init__(self,name): 
        self.name = name
    def show(self):
        print(f"The name of the student  is {self.name}")   

class div_B:
    def __init__(self,roll_no):
        self.roll_no = roll_no
    def show(self):
        print(f"The roll no. of the student  is {self.roll_no}") 


class Students(div_B,div_A):
    def __init__(self, name,roll_no):
      self.roll_no = roll_no
      self.name = name


a=Students("Sanjay",7)
print(a.name)
print(a.roll_no)
a.show()
print(Students.mro())    #mro= method resolution order





