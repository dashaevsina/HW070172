# Chapter 6, Programming exercise 6
# This program calculates the area of  
# a traingle given the length of its 
# three sides using functions.

import math

def triangle(a, b, c):
    s = (a + b + c) / 2
    A = math.sqrt (s * (s - a) * (s - b) * (s - c))
    return A

def main():
    print("This program calculates the area of \n a triangle given the lenght of its \n three sides.")
    a, b, c = eval(input("Enter the length of the three sides of the triangle (separated by a comma): "))
    A = triangle(a, b, c)
    print("The area of the triangle is", round(A, 2), ".")

main()