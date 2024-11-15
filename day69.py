class Employee:
    company="Apple"
    def show(self):
        print(f"The name is {self.name} and company is {self.company}") # type: ignore

    @classmethod   #to change the class
    def chnageCompany(cls, newCompany):
        cls.company= newCompany

e1= Employee()
e1.name="Soniya"  # type: ignore
e1.show()
e1.chnageCompany("Tesla")
e1.show()
print(Employee.company)
