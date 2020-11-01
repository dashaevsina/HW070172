# Chapter 3, Programming exercise 9
# This program calculates the area of  
# a traingle given the length of its 
# three sides. 

import math

def main():
    print("This program calculates the area of \n a triangle given the lenght of its \n three sides.")
    a, b, c = eval(input("Enter the lenght of the three sides of the triangle (separated by a comma): "))
    s = (a + b + c) / 2
    A = math.sqrt (s * (s - a) * (s - b) * (s - c))
    print("The area of the triangle is", round(A, 2), ".")

main()