'''
MULTILEVEL INHERITANCE:
derived from the child class ,this chain can be multiple, for eg: parent class, chlid class, chlid's child class
'''


class Animal:
    def __init__(self,name, species):
        self.name = name
        self.species = species
    def show(self):
        print(f"Name: {self.name}")
        print(f"Species: {self.species}")

class Dog(Animal):
    def __init__(self, name, breed):
        self.breed = breed 
        Animal.__init__(self,name, species="Dog")
    def show(self):
        Animal.show(self)
        print(f"Breed= {self.breed}")

class GoldenRetriever(Dog):
    def __init__(self, name, colour):
        self.colour = colour
        Dog.__init__(self,name, breed ="Golden Retriever") 
    def show(self):
        Dog.show(self)
        print(f"Colour: {self.colour}")

a=GoldenRetriever("dog","orange")
a.show()
