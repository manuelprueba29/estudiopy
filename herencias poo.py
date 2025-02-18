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
class vehicle:
    
    def __init__(self, brand, model, price):
        self.brand=brand
        self.model=model
        self.price=price
        self.is_available=True
        
        
    def sell(self):
        if self.is_available:
            self.is_available=False
            print(f"la marca {self.brand} ha sido vendida")
        
        else:
            print(f"El evhiculo {self.brand}. No esta disponible")
            
    def check_available(self):
        return self.is_available
    
    def get_price(self):
        return self.price
    
    def start_engine(self):
        raise NotImplementedError("Este metodo debe ser implementado pór la subclase")
    
    def stop_engine(self):
        raise NotImplementedError("Este metodo debe ser implementado pór la subclase")
        
        
class car(vehicle):
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
        
class Bike(vehicle):
           
           def start_engine(self):
             
               if  self.is_available:
                   return f"La bicicleta {self.brand} esta en marcha"
               else:
                   return f"La bicicleta {self.brand} no esta disponible"
               
           def stop_engine(self):
               if self.is_available:
                   return f"La bicicleta{self.brand}  se ha detenido "
               else:
                   return f"La bicicleta {self.brand} no esta disponible"
               
class Truck(vehicle):
    
    def start_engine(self):
      
        if  self.is_available:
            return f"El Camion{self.brand} esta en marcha"
        else:
            return f"El Camion {self.brand} no esta disponible"
        
    def stop_engine(self):
        if self.is_available:
            return f"El Camion {self.brand}  se ha detenido "
        else:
            return f"El Camion {self.brand} no esta disponible"
        
class Customer:
    def __init__(self, name):
        #comprador
        self.name=name
        self.purchased_vehicle = []
        
    def buy_vehicle(self, vehicle: vehicle):
        
        if vehicle.check_available():
            vehicle.sell()
            self.purchased_vehicle.append(vehicle)
        else:
            print(f"Lo siento, {vehicle.brand} no esta disponible")
            
    def inquire_vehicle(self, vehicle:vehicle):
        if vehicle.check_available():
            availablity= "DIsponible"
        else:
            availablity= "No disponible"
        
        print(f"El {vehicle.brand} esta {availablity} y cuesta  {vehicle.get_price()} ")
        
class Dealership:
    
    def __init__(self):
        self.inventory = []
        self.customer = []
        
    def add_vehicles(self, vehicle:vehicle):
        self.inventory.append(vehicle)
        print(f"El {vehicle.brand} ha sido añadido al inventario")
        
    def register_customers(self, customer: Customer):
        self.customer.append(customer)
        print(f"El cliente {customer.name} ha sido añadido")
        
    def show_available_vehicle(self):
        print("Vehiculos disponible en la tienda")
        for vehicle in self.inventory:
            if vehicle.check_available():
                print(f"- {vehicle.brand} por {vehicle.get_price}")
        
    
           
        
        
        
        
    
    
    
    
        
    
            
            
            
