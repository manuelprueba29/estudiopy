# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 16:24:27 2025

@author: manuel.moreno
"""

""" 
divisor=int(input("ingrese el numero"))
resultrado=100/divisor
print(resultrado)
"""

try:
  divisor=int(input("Ingrese un numero divisor"))
  resultado= 100/divisor
  print(resultado)
except ZeroDivisionError as e:
    print("error el divisor no puede ser cero")
    print("Ha ocurrido un error", e)
except ValueError as e:
    print("Debes introducir un numero valido", e)
    
