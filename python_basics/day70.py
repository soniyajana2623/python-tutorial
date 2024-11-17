class Employee:
    def __init__(self,name,salary,id):
        self.name= name
        self.salary= salary
        self.id= id
    
    @classmethod
    def fromStr(cls,string):
        return cls(string.split("-")[0],string.split("-")[1],string.split("-")[2])

e1=Employee("Soniya","Rs.20000",2623)
print(e1.name)
print(e1.salary)
print(e1.id)

a = "Sanjay-30000-7797"
b = "Sumitra-20000-1611"
e2=Employee.fromStr(a)
e3=Employee.fromStr(b)
print(e2.name)
print(e2.salary)
print(e2.id)
print(e3.name)
print(e3.salary)
print(e3.id)

