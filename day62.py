'''
ACCESS SPECIFIERS/MODIFIERS:
It is used to limit access class variables and class methods outside
of the class while implementing the concept of inheritance

1.Public
2.Private
3.Protected
'''


'''
PUBLIC:
It is by default public. Any instance followed by 'self' keyword in the function are public accessed
'''
class Employee:
    def __init__(self,name,age):
        self.name="Soniya"    #public access
        self.age= 21          #public access

a=Employee("Soniya",21)
print(a.name)
print(a.age)

'''
PRIVATE:(Mangling)
Which are only accessable inside the class.We cannot use private member outside the class
By adding '__' in prefix
'''
class a1:
    def __init__(self):
        self.__name= "Sanjay"
        self.__age= 27
a=a1()
# print(a.name)  cannot be accessed directly
print(a._a1__name)  #can be accessed indirectly # type: ignore
print(a._a1__age)   #can be accessed directly # type: ignore

'''
PROTECTED:
used by '_' prefix

'''
class Exam():
    def __init__(self):
        self._name="Soniya"
        self._score= '80/100'
b=Exam()
print(b._name)
print(b._score)



         


