#Gestion de bibliote

#clase libro: Autor, fecha, descripcion
#clase persona. prestar y devolver libro
#clase biblioteca que va agestionar un conjunto de libros y conjunto de usuarios 

class Book:
    
    def __init__(self, title, author):
        self.title = title
        self.author= author
        self.available=True
        
    def borrow(self):
        
        if self.available:
            self.available=False
            print(f"El libro ha sido {self.title} ha sido prestado")
        
        else:
            print(f"El libro {self.title} no esta disponible")
            
    def return_book(self):
        if self.available==False:
            self.available=True
            print(f"Libro {self.title} devuelto por lo tanto esta libre")

class User:
    def __init__(self, Name, Userid):
        
        self.Name= Name
        self.Userid=Userid
        self.borrowed_books=[]
        
    def borrow_books(self, book):
        
        if book.available:
            book.borrow()
            book.title
            self.borrow_books.append(book)
            
        
        else:
            print(f"El libro{book.title} no esta disponible")
        
        
        
            