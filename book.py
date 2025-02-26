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

    def return_book(self, book):
        if book in self.borrow_books:
            book.return_book()
            self.borrow_books.remove(book)
        else:
            print(f"El libro {book.title} No esta en la lista de prestados")

class library:
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self, Book):
        self.books.append(Book)
        print(f"El libro {Book.title} ha sido agregado")
    
    def registre_user(self, user):
        self.users.append(user)
        print(f"El usuario {user.name} ha sido registrado")

    def show_available_books(self):
        
    
        print("LIbros disponibles")
        for book in self.add_book:
            if book.available:
                print(f"{book.title} por {book.author}")


book1=Book("EL principito", "Antoine de sain-exuper")
book2=Book("1984", "george orwel")

#crear usuario

user1=User("carli", "001")

library= library()
library.add_book(book1)
library.add_book(book2)
library.registre_user(user1)

#mostrar libros
library.show_available_books()

#realizar prestamo
user1.borrow_books(book1)

library.show_available_books()

#devolver libro
library.return_book(book1)


library.show_available_books()






        
        
        
            