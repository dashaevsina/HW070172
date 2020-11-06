# Chapter 6, Programming exercise 5
# This program calculates the cost 
# per square inch of a ciruclar pizza
# using functions, given its diameter 
# and price.

import math 

def areaOfPizza(diameter):
    area = math.pi * ((.5 * diameter) ** 2)
    return area

def priceOfPizza(price, area):
    price_per_square_inch = price / area
    return price_per_square_inch

def main():
    print("This program will calculate the cost \n per square inch of a circular pizza \n given its diameter and price.")
    print()
    price = float(input("Please enter the cost of the pizza: "))
    diameter = float(input("Please enter its diameter: "))
    A = areaOfPizza(diameter)
    price_per_square_inch = priceOfPizza(price, A)
    print ("The price of the pizza per square inch is €{0}.".format(round(price_per_square_inch, 2)))

main()    