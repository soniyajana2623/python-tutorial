class library:
    def __init__(self,books,no_of_books):
        self.books=books
        self.no_of_books=no_of_books
    
    def show_no(self):
        print(f"The number of books: {self.no_of_books}")
        for book in self.books:
            print(book)
    
    def check(self):
        if self.books==self.no_of_books:
            print(True)
        else:
            print(False)
    

book=(["It ends with us","Rich dad poor dad","Atomic habbits","Ikigai"])
a=library(book,len(book))
a.show_no()
a.check

