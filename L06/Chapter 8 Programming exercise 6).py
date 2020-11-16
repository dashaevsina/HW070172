# Chapter 8, programming exercise 6
# This program determines finds every prime
# number less than or equal to n.

import math

def primeNumber(n):
    x = math.sqrt(n)
    i = 2

    while i <= x:
        value = n % i 
        if value == 0:
            return
        else:
            i = i + 1
    print("The number", n, "is prime.")


def main():
    print("This program will determine if a value is prime.\n NB: The program will quit if the value isn't prime!\n")
    x = 0
    while True:
        x = int(input("Enter a positive whole number as the n value: "))
        
        if (x == 0) or (x < 1) or (x % 1 != 0):
            x = int(input("Please enter a whole number higher than 0: "))
        else:
            break
    for n in range(x):
        primeNumber(n + 1)
    
main()