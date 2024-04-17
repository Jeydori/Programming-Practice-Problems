#Repititive Problem 1
import math


integer = int(input('Enter a positive integer: '))
factorial = 1

if integer >= 1:
    for i in range(1, integer + 1):
        factorial = factorial*i
    
print(factorial)