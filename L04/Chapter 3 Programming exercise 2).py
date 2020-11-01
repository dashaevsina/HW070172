# Chapter 3, Programming exercise 2
# This program calculates the cost 
# per square inch of a ciruclar pizza, 
# given its diameter and price

import math 

def main():
    print("This program will calculate the cost \n per square inch of a circular pizza \n given its diameter and price.")
    print()
    price = float(input("Please enter the cost of the pizza: "))
    diameter = float(input("Please enter its diameter: "))
    area = math.pi * ((.5 * diameter) ** 2)
    price_per_square_inch = price / area
    print ("The price of the pizza per square inch is", round(price_per_square_inch, 2), ".")

main()    