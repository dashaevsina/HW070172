# Chapter 3, Programming exercise 6
# This program calculates the slope of  
# a line through two (non-vertical) points.

import math

def main():
    print("This program calculates the slope of \n a line through two (non-vertical) points.")
    x1, y1 = eval(input("Enter the first values for x and y (separated by a comma): "))
    x2, y2 = eval(input("Enter the second values for x and y (separated by a comma): "))
    slope = (y2 - y1) / (x2 - x1)
    print("The slope of the line is", slope, ".")

main()