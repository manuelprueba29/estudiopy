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
            print(f"El libro  {self.title} ha sido prestado")
        
        else:
            print(f"El libro {self.title} no esta disponible")
            
    def return_book(self):
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
            self.borrow_books.append(book)
        
        else:
            print(f"El libro{book.title} no esta disponible")
    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.return_book()
        else:
            print(f"El libro {book.title} no esta en la lista de libros prestados para el usuario {self.Name}")
            
class Biblioteca:
    
    def __init__(self, Name):
        
        self.Name=Name
        self.libros=[]
        self.User=[]
        self.prestamos={}
        
    def AggLibros(self, book):
        if book not in self.libros:
            self.libros.append(book)
            print(f"El libro {book.title} ha sido agregado")
        else:
            print(f"El libro {book.title} ya se encuentra en la base de datos")
            
    def DeleteLibro(self, book):
        if book in self.libros:
            self.libros.remove(book)
            print(f"El libro {book.title} ha sido eliminado")
        else:
            print(f"El libro {book.title} no se encuentra en la base de datos  por lo tanto no se puede eliminar")
            
    def searchLibro(self, book):
        if book in self.libros:
            print(f"Los datos del libro {book.title} son {book}")
            
    def RegistreUser(self, user):
        
        if user not in self.User:
            self.User.append(user)
            print(f"Usuario {user.Name} Registrado")
        else:
            print(f"El usuario {user.Name} ya se encuentra registrado")
            
    def RegistreDates(self, user, book):
        if user in self.User and book in self.libros:
            if book.available:
                book.borrow() # Marca el libro como prestado
                
                if user not in self.prestamos:
                    self.prestamos[user]=[]# si el usuario no tiene préstamos, inicializa una lista
                self.prestamos[user].append(book)# Agrega el libro a lista del usuario
                print(f"El usuario{user.Name} ha tomado prestado el libro {book.title}")
                
            else:
            
                print("El libro ya esta prestado")
                
        else: 
            print(f"Usuario {user.Name} o libro {book.title} no encontrado")
            
            
book1 = Book("1984", "george orwel")
book2 = Book("Ciend años de soledad", "Gabriel Garcia Marquez")

Biblioteca_San_Martin=Biblioteca("San Martin")
Biblioteca_San_Martin.AggLibros(book1)
Biblioteca_San_Martin.AggLibros(book2)
                
                
                
                
                
                
                
                    
        
            
            
            
            
            
    
        
        
    
        
        
        
        
        
        
        
#Cuando ejecutamos book1 = Book("1984", "George Orwell"), creamos una instancia de Book con title y author.
# Luego, cuando hacemos user1.borrow_books(book1), pasamos la instancia completa como argumento.
#borrow_books(self, book) solo recibe una variable (book), que es una referencia al objeto book1
#Dentro de borrow_books(), podemos acceder a los atributos desde el objeto book, por ejemplo /print(book.title)  #  Esto imprimirá "1984"

#La razon por la que si pongo book.title en borro_book me imprime el titulo del libro es porque el argumento book en realidad es una instancia del objeto book-
#Esto conlleva a que book tenga tanto title,author y available
          