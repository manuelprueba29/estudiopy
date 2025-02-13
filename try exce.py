# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 14:51:30 2025

@author: manuel.moreno
"""


add = lambda a , b: a+ b
print(add(10, 4))


multiply = lambda a, b: a* b

print(multiply(80,5))

resta=lambda a, b: a - b
print(resta(80, 5))

cuadrado= lambda a, b: (a**b)
print(cuadrado(80,5)-resta(80,5))

#cuadrado de cada numero 

numbers = range(11)
squared_numers = list(map(lambda x: x**2, numbers))
print(squared_numers)


#Pares
pares=list(filter(lambda x: x%2==0, numbers))
print("filttro:", pares)

# factorial de un numero utilizando recursividad en una funcion

def factorial(n):
    if n==0:
        return 1
    else: 
      alamacenamiento= n*factorial(n-1)
      print(alamacenamiento)
      return(alamacenamiento)
  

print("factorial", factorial(3))

# Serie de Fibonacci
# F (N-1) + F (N-2)

def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))


        
        
        
        