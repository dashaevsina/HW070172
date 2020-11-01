# Chapter 3, Programming exercise 7
# This program calculates the distance  
# between two (non-vertical) points.

import math

def main():
    print("This program calculates the distance \n between two (non-vertical) points.")
    x1, y1 = eval(input("Enter the first values for x and y (separated by a comma): "))
    x2, y2 = eval(input("Enter the second values for x and y (separated by a comma): "))
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    print("The distance between the two points is", distance, ".")

main()