# Chapter 8, programming exercise 7
# This program works based on the 
# Goldbach conjecture (which asserts
# that every even number is the sum of
# two prime numbers). 

from math import sqrt

def primeNumber(n):
    primeNumber = True
    for i in range(2, round(sqrt(n) +1)):
        if n % i == 0:
            primeNumber = False
            break
    return primeNumber

def main():
    print("\nThis program works based on the Goldbach conjecture.\n It'll get a number from the user, check to make sure that it's even, \n and then find 2 prime numbers that add up to that number.\n")
    n = int(input("Enter a positive even integer as the n value: "))

    if n > 2:
        listOfPrimes = []
        for i in range (2, n + 1):
            if primeNumber(i):
                listOfPrimes.append(i)

        done = False
        for i in listOfPrimes:
            for x in listOfPrimes:
                if i + x == n:
                    print("The Goldbach partitions are the following: ", i, "+", x, "=", n) 
                    done = True
                    break      
            if done:
                break 
    else:
        print("The value has to be greater than 2.")        

if __name__ == '__main__':
    main()