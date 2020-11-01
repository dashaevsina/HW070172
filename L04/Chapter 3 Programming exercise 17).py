# Chapter 3, Programming exercise 17
# This program implements Newton's method
# and uses the guess-and-check approach
# when computing square roots.

import math

def main():
    print("This program implements Newton's method to guess the square root of a number.")
    x = eval(input("Enter a value for the calculation: "))
    y = eval(input("Enter the number of times to improve the guess: "))
    guess = x / 2
    for i in range (y):
        guess = (guess + x / guess) / 2
    print("The estimated value of the square root is", guess, ", \n whereas the actual square root is", (guess - math.sqrt(x)))

main()