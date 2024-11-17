class details:
    name="soniya"
    age= 21
    def person(self):  #The self parameter is a reference to the current instance of the class,
        #  and is used to access variables that belongs to the class.
       print(f"{self.name} is {self.age} years old ")
    
    
a=details()
b=details()
c=details()
d=details()

a.name="Nikita"
a.age= 20

b.name="Sanjay"
b.age= 27

c.name="Vishwam"
c.age= 6

# d.name="Varnika"
# d.age= 10

# object=details()
# print(object.name)
# print(object.age)
# object.person()
a.person()
b.person()
c.person()
d.person()

