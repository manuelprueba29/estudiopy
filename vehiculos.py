# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 09:41:40 2025

@author: manuel.moreno
"""

# concepcionaria de vehiculos. compra y venta de vehiculos.
# Ademas gestionar un vehiculo. los usuarios podran consultar cuales estan disponibles
#cual es el precio y tambien comprar uno

#Debe existir la clase vehiculo, la clase user, clase concepcionario

class Vehiculo:
    
    def __init__(self, vehicle_type, color, plate, brand, model, door_number):
        
        self.vehicle_type=vehicle_type
        self.color=color
        self.plate=plate
        self.brand=brand
        self.model=model
        self.door_number=door_number
      
        
        
    def MostrarInfo(self):
        print(f"tipo de vehiculo {self.vehicle_type} , color: {self.color},  placa: {self.plate}, marca: {self.brand}, modelo: {self.model}, nro de puertas: {self.door_number}")
      
class User:
    
    def __init__(self, Name, Email, Id):
        
        self.Name=Name
        self.Email=Email
        self.Id=Id
        self.vehicles_purchases= None # Historial no creado aun
        
    def MostrarInfoUser(self):
        print(f"Nombre: {self.Name} Email: {self.Email} Id:{ self.Id} ")
        

        
class User_History:
    
    def __init__(self, user):
        
        self.user=user
        self.vehicles_purchases={} # vehiculos comprados
        
    def vehicle_purchase(self, vehicle):
        
        if vehicle.plate not in self.vehicles_purchases:
            self.vehicles_purchases[vehicle.plate]=vehicle
            print(f"el vehiculo con placa {vehicle.plate} ya fue  comprado por {self.user.Name}")
        
        else:
            print(f"EL vehiculo con placa ya fue comprado por el usuario {self.user.Name}")
            
    def Vehicle_list(self):
        if not self.vehicles_purchases:
            print(f"El user {self.user.Name} no ha comprado ningun carro")
            return
        print(f"vehiculo comprado por {self.user.Name}")
        for palte, vehicle in self.vehicles_purchases.items():
            print(f"Vehicle purchase: {vehicle.brand} {vehicle.model}, placa:{vehicle.plate}") # revisar y entender muestra la referencia de el vehiculo que comro el usario
            

class UserGestor:
    
    def __init__(self):
        
        self.Users={}
       
        
    def aggUser (self, user ):
        
        if user not in self.Users:
            self.Users[user.Id]= User #forma en la que se guarda el usuario de la clase User. instanciando user
            user.MostrarInfoUser()
            #print(f"El usuario {user.Name} ha sido agregado ")
        
        else:
            print(f"El usuario {user.Name} con ID {user.Id} ya existe")
            
    def DeleteUser(self, Id):
        
        if Id in self.Users:
            user=self.Users[Id]
            del self.Users[Id]
            print(f"El usuario {user.Name}  con  {Id} ha sido eliminado")
        
        else:
            print(f"El usuario con id {Id} no se encuentra en la lista. No eliminado")
            
    def UpdateUser(self, Id):
        
        if Id in self.Users:
            user=self.Users[Id]
            print("Por favor indicar que dato desea actualizar" )
            print("1. Nombre")
            print("2. Email")
            
            try:
                
                opcion= int(input("Selecione una opcion 1 o 2"))
                
            except ValueError:
                print("Entrada no valida debe ingresar 1 o 2")
                return
            
            if opcion == 1:
                
                newUser=input("Escribe el nombre y presioa enter para continuar: ")
                user.Name=newUser
                print(f"Nombre Actualizado {newUser}")
            
            elif opcion == 2:
                
                newEmail=input("Escribe el nuevo email que deseas actualizar: ")
                user.Email=newEmail
                print(f"Email actualizado {newEmail}")
                
            else:
                print("La opcion seleccionada no es valida")
                
        else:
            print(f"El id {Id} no fue encontrado")
            
    def searchUser(self, Id):
         if Id in self.Users:
             user=self.Users[Id]
             user.MostrarInfo() # se llama la funcion mostrar info de User entender bien el concepto
             print(f"Los datos del Usuario son: {user.Name}")
        
         else:
            print(f"El Id {Id} no fue encontrado")
            
    def ListUser(self):
        if not self.Users:
            print("No hay usuarios registrados")
            
        else:           
            for user in self.Users.values():
                user.MostrarInfo() # Llamamos a la función de cada usuario entender bien el concepto
             
            
            
class GestionConcepcionario: 
    def __init__(self, name):
        self.name = name
        self.inventario = {}  # Diccionario de vehículos disponibles
        self.ventas = []  # Lista de vehículos vendidos
        self.empleados = []  # Lista de empleados registrados
    
    def agregar_vehiculo(self, vehiculo):
        """Agrega un vehículo al inventario."""
        if vehiculo.plate not in self.inventario:
            self.inventario[vehiculo.plate] = vehiculo
            print(f"Vehículo {vehiculo.brand} {vehiculo.model} agregado al inventario.")
        else:
            print(f"El vehículo con placa {vehiculo.plate} ya está en el inventario.")
    
    def listar_vehiculos_disponibles(self):
        """Lista los vehículos disponibles en el inventario."""
        if not self.inventario:
            print("No hay vehículos disponibles en el concesionario.")
        else:
            print("Vehículos disponibles:")
            for vehiculo in self.inventario.values():
                vehiculo.MostrarInfo()
    
    def vender_vehiculo(self, placa, usuario):
        """Vende un vehículo a un usuario, lo elimina del inventario y lo agrega al historial del usuario."""
        if placa in self.inventario:
            vehiculo = self.inventario.pop(placa)  # Eliminar el vehículo del inventario
            self.ventas.append(vehiculo)  # Agregarlo a la lista de ventas
            usuario_historial = User_History(usuario)  # Crear historial si no existe
            usuario_historial.vehicle_purchase(vehiculo)  # Registrar la compra
            print(f"Vehículo {vehiculo.brand} {vehiculo.model} vendido a {usuario.Name}.")
        else:
            print(f"No se encontró un vehículo con placa {placa}.")
    
    def registrar_empleado(self, empleado):
        """Registra un nuevo empleado en el concesionario."""
        if empleado.Id not in [e.Id for e in self.empleados]:
            self.empleados.append(empleado)
            print(f"Empleado {empleado.Name} registrado correctamente.")
        else:
            print(f"El empleado con ID {empleado.Id} ya está registrado.")
    
    def listar_empleados(self):
        """Lista los empleados del concesionario."""
        if not self.empleados:
            print("No hay empleados registrados en el concesionario.")
        else:
            print("Lista de empleados:")
            for empleado in self.empleados:
                empleado.MostrarInfoUser()

            
vehiculo1=Vehiculo("Camioneta", "Rojo", "Dre76f", "Mazda", "2025", "Cuatro puerta")    
vehiculo1.MostrarInfo()   



user1=User("Manuel", "manuel199729♠4gmail.com", "1035437457")

historial1=User_History(user1)

historial1.vehicle_purchase(vehiculo1)

historial1.Vehicle_list()

Gestionando1=UserGestor()

Gestionando1.aggUser(user1)   
            
            
    
        
        
        
        
        
        
        
        
        
        
        
        
        