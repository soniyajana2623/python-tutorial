'''
dir(), __dict__, help() Methods in pyhton
'''

'''
 dir():
'''
x=[1,2,3,4]
print(dir(x))


'''
 __dict__: forms into a dictionary
'''
class Person:
    def __init__(self,name,age):
        self.name= name
        self.age= age
a=Person("Soniya", 21)
print(a.name)
print(a.__dict__)



'''
help():
'''
class Person1:
    def __init__(self,name,age):
        self.name= name
        self.age= age
a=Person("Soniya", 21)
print(help(Person1))