# Chapter 6, Programming exercise 7
# This program computes the nth Fibonacci 
# number using functions.   

import math

def fibonacci(n):
    x = 0
    y = 1
    z = 0

    for i in range (n+1):
        z = x + y
        x = y
        y = z
    return y
def main():
    print("This program computes the nth Fibonacci number.")
    n = eval(input("Enter the desired number in the Fibonacci sequence: "))
    y = fibonacci(n)
    print("The {0} number in the Fibonacci sequence is {1}.". format(n, y))

main()