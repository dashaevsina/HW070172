# Chapter 3, Programming exercise 12
# This program calculates the sum of  
# the cubes of the first n natural numbers.

import math

def main():
    print("This program calculates the sum of \n the cubes of the first n natural numbers.")
    n = int(input("Enter the value of n (a whole number): "))
    total = 0
    for i in range(1, n+1):
        total = total + i ** 3
    print("The sum of the cubes of the first", n, "integers is", total, ".")

main()