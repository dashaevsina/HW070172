# Chapter 3, Programming exercise 16
# This program computes the nth Fibonacci number.   

import math

def main():
    print("This program computes the nth Fibonacci number.")
    n = eval(input("Enter the desired number in the Fibonacci sequence: "))
    x = 1
    y = 0
    for i in range (n+1):
        z = x + y
        x = y
        y = z
    print("The", i, "number in the Fibonacci sequence is" ":", y, ".")

main()