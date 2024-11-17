'''
Hierarchical Inheritance: 
            A
   -------------------------
   |           |           |
   B           C           D
 
'''

class Animal:
    def __init__(self,name,breed):
        self.name = name 
        self.breed= breed
    def show(self):
        print(f"The animal is {self.name} ")
        print(f"The breed is {self.breed}")


class Dog(Animal):
    def __init__(self, name ,colour):
        self.colour = colour
        Animal.__init__(self,name, breed="Golden retriever")
    def show(self):
        Animal.show(self)
        print(f"The colour of the dog is {self.colour}")


class Cat(Animal):
    def __init__(self, name ,colour):
        self.colour = colour
        Animal.__init__(self,name, breed="Persian")
    def show(self):
        Animal.show(self)
        print(f"The colour of the cat is {self.colour}")

class bark(Dog):
    def __init__(self, name, sound):
        Dog.__init__(self,name, colour="Black")
        self.sound = sound
    def show(self):
        Dog.show(self)
        print(f"The Sound of the dog is {self.sound}")
    

class sound(Cat):
    def __init__(self, name, sound):
        Cat.__init__(self,name, colour="Orange")
        self.sound = sound
    def show(self):
        Cat.show(self)
        print(f"The Sound of the cat is {self.sound}")

a=sound("Cat","Meow")
a.show()
b=bark("Dog","Bark")
b.show()
    