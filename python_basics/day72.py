'''
SUPER KEY WORD:
It is used to refer to the parent class. It is useful when a class inherits from
multiple parent class and you want to call method from one of it.
Child class can use function of parent class by using "super()" key
'''


class ParentClass:
    def parent_method(self):
        print("This is the parent method.")

class ChlidClass(ParentClass):
    def parent_method(self):
        print("Soniya")
        super().parent_method() 
    def child_method(self):
            print("This is the chlid method")
            super().parent_method()  

child=ChlidClass()
child.child_method()
child.parent_method()