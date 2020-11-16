# Chapter 8, programming exercise 1
# This program computes and outputs the
# nth Fibonnaci number. 

import math

def main():
    print("This program computes the nth Fibonacci number.")
    nthFibonacciNumber = int(input("\nEnter the number in the Fibonacci sequence that \n you would like to generate: "))
    count = 0
    x = 1
    y = 0

    while count < nthFibonacciNumber:
        count = count + 1
        z = x + y 
        x = y
        y = z
    print("The", nthFibonacciNumber, "number in the Fibonacci sequence is: ", z, ".")

main()