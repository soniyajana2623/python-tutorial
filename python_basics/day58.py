# CONSTRUCTORS  __int__()
class person:

    def __init__(self,n,a): #parameterized contructors    #a=person("Soniya",21)
                               #b=person
        ("Sanjay", 27)
        print("Hello")
        self.name=n
        self.age=a
    
    
    def info(self):                                                  # a.info()
                                                                     # b.info()
        print(f"{self.name} is {self.age} years old")

a=person("Soniya",21)
b=person("Sanjay", 27)

a.info()
b.info()