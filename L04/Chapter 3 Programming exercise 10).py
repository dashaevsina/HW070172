# Chapter 3, Programming exercise 10
# This program calculates the length of  
# a ladder required to reach a given height
# when leaned against a house.

import math

def main():
    print("This program calculates the length of \n a ladder required to reach a given height \n when leaned against a house.")
    height = float(input("Enter the height of the ladder (in feet): "))
    angle = float(input("Enter the angle of the ladder (in degrees): "))
    length = height / (math.sin((math.pi / 180 * angle)))
    print("The ladder is", round(length, 2), "feet in length.")

main()