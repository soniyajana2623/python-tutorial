class library:
    def __init__(self):
        self.books=[]
        self.no_of_books = 0
       
    
    def show_no(self,book):
        self.books.append(book)
        self.no_of_books=len(self.books)

    def showinfo(self):
        print(f"The library has {self.no_of_books} books. The books are")
        for book in self.books:
            print(book)

    

a=library()
a.show_no("Ikigai")
a.show_no("Atomic habbits")
a.show_no("It ends with us")
a.show_no("Rich dad poor dad")
a.showinfo()





