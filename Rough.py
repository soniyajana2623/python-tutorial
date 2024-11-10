# class Employee:
#     def __init__(self):
#         self.__name="Soniya"

# a=Employee()
# # print(a.__name)
# print(a._Employee__name)

class Library:
	def __init__(self,books,Noofbooks):
		self.books=books
		self.Noofbooks=Noofbooks
	def Info(self):
		print(f"Books i have readean are {self.books} and they are about {self.Noofbooks} of them")
	def check(self):
		if len(self.books)==self.Noofbooks :
			print("True")
		else :
			print("False")



a=Library(["Rich dad poor Dad","idk"],2)
a.Info()
a.check




