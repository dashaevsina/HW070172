# Chapter 8, programming exercise 5
# This program determines if a value of 
# n is prime. 

import math

def main():
    print("This program will determine if a value is prime.\n NB: The program will quit if the value isn't prime!\n")
    n = int(input("Enter a positive whole number as the n value: "))

    while (n == 0) or (n < 1) or (n % 1 != 0):
        n = int(input("Please enter a whole number higher than 0: "))
    
    x = math.sqrt(n)
    i = 2

    while i <= x:
        value = n % i 
        if value == 0:
            exit()
        else:
            i = i + 1
    print("The number is prime.")
    
main()