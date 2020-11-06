# Chapter 6, Programming exercise 8
# This program implements Newton's method
# and uses the guess-and-check approach
# when computing square roots using functions.

import math

def nextGuess(guess, x):
    guess = (guess + x / guess) / 2
    return guess

def main():
    print("This program implements Newton's method to guess the square root of a number.")
    x = eval(input("Enter a value for the calculation: "))
    y = eval(input("Enter the number of times to improve the guess: "))
    guess = x / 2
    for i in range (y):
        guess = nextGuess(guess, x)
    print("The estimated value of the square root is", guess, ".")

main()