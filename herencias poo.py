# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 16:30:26 2025

@author: manuel.moreno

crear la clase vehicle con su constructor (brand, model, price)

crear el metodo vender
crear el metodo consultar el estado de disponibilidad 
devolvemos el precio del precio
crear dos metodos
*iniciar el funcionamiento de los vehiculos(todos)
* detener el funcionamiento

"""

# aqui se explica toda la teoria de herencia y muestra a la clase padre que en este caso es vehiculo(Esto es polimorfismo)
"""
El polimorfismo en programación orientada a objetos se refiere a la capacidad de una clase derivada de modificar el comportamiento de un método heredado de su clase base. 
En este caso:
La clase padre Vehicle define los métodos start_engine y stop_engine, pero como métodos abstractos (con raise NotImplementedError).
Las subclases (Car, Bike, Truck) implementan estos métodos con su propio comportamiento.
Al llamar start_engine o stop_engine en un objeto de cualquier subclase, se ejecutará la versión correspondiente según el tipo de vehículo.

"""
class Vehicle:
    
    def __init__(self, brand, model, price):
        self.brand=brand
        self.model=model
        self.price=price
        self.is_available=True
        
        
    def sell(self):#vender
        if self.is_available:
            self.is_available=False
            print(f"la marca {self.brand} ha sido vendida")
        
        else:
            print(f"El evhiculo {self.brand}. No esta disponible")
            
    def check_available(self):#listar disponibles
        return self.is_available
    
    def get_price(self): # obtener precio
        return self.price
    
    def start_engine(self):  # iniciar motor
        raise NotImplementedError("Este metodo debe ser implementado pór la subclase") #esto es una excepcion
    
    def stop_engine(self):  # parar motor
        raise NotImplementedError("Este metodo debe ser implementado pór la subclase") #esto es una excepcion
        
        
class car(Vehicle):
    def start_engine(self):
      
        if  self.is_available:
            return f"El motor{self.brand} esta en marcha"
        else:
            return f"El coche con {self.brand} no esta disponible"
        
    def stop_engine(self):
        if self.is_available:
            return f"El motor {self.brand}  se ha detenido "
        else:
            return f"El coche {self.brand} no esta disponible"
        
class Bike(Vehicle):# clase vicicleta
          
           def start_engine(self): #arrancar el motor
             
               if  self.is_available:
                   return f"La bicicleta {self.brand} esta en marcha"
               else:
                   return f"La bicicleta {self.brand} no esta disponible"
            
           def stop_engine(self):#parar el motor   
               if self.is_available:
                   return f"La bicicleta{self.brand}  se ha detenido "
               else:
                   return f"La bicicleta {self.brand} no esta disponible"
               
class Truck(Vehicle): #clase camion
  
    def start_engine(self):  #arrancar camion
      
        if  self.is_available:
            return f"El motor del Camion{self.brand} esta en marcha"
        else:
            return f"El motor del Camion {self.brand} no esta disponible"
    
    def stop_engine(self):  #parar camion  
        if self.is_available:
            return f"El motor del Camion {self.brand}  se ha detenido "
        else:
            return f"El motor del Camion {self.brand} no esta disponible"
        
class Customer: #clase cliente comprador
    
  
    def __init__(self, name):
        
        self.name=name
        self.purchased_vehicle = []
      
    def buy_vehicle(self, vehicle: Vehicle): #comprar vehiculo 
        
        if vehicle.check_available():
            vehicle.sell()
            self.purchased_vehicle.append(vehicle)
        else:
            print(f"Lo siento, {vehicle.brand} no esta disponible")
          
    def inquire_vehicle(self, vehicle:Vehicle): # consultar disponibilidad de vehiculo 
        if vehicle.check_available():
            availablity= "Disponible"
        else:
            availablity= "No disponible"
        
        print(f"El {vehicle.brand} esta {availablity} y cuesta  {vehicle.get_price()} ")
       
class Dealership:  # clase  concesionario
    
    def __init__(self):
        self.inventory = []#inventario
        self.customer = []#cliente
        
    def add_vehicles(self, vehicle:Vehicle): #agregar vehiculo
      
        self.inventory.append(vehicle)
        print(f"El {vehicle.brand} ha sido añadido al inventario")
        
    def register_customers(self, customer: Customer): #registar clientes
       
        self.customer.append(customer)
        print(f"El cliente {customer.name} ha sido añadido")
        
    def show_available_vehicle(self):# mostar vehiculos disponibles
        
        print("Vehiculos disponible en la tienda")
        for vehicle in self.inventory:
            if vehicle.check_available():
                print(f"- {vehicle.brand} por {vehicle.get_price()}")


car1=car("mazda" , "2025", 10000)
biker1=Bike("yamaha", "mx", 10000)
truck1=Truck("mercedez", "2015", 20000)

cliente1=Customer("Manuel")

#cliente1.buy_vehicle(car1)

Dealership1=Dealership()

Dealership1.add_vehicles(car1)
Dealership1.add_vehicles(biker1)
Dealership1.add_vehicles(truck1)


#MOstrar vehiculos disponibles

Dealership1.show_available_vehicle()

# 4 fundamentos de la programacion orientada a objetos herencia. abstraccion, encapsulamiento y polimorfismo. en la clase 27 empiezan a explicar el polimorfismos 





        
    
           
        
        
        
        
    
    
    
    
        
    
            
            
            
