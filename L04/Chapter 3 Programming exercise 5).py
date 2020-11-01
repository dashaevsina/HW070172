# Chapter 3, Programming exercise 5
# This program calculates the cost of  
# an order at the Konditorei coffee shop.

import math

def main():
    print("This program calculates the cost of \n an order at the Konditorei coffee shop.")
    pounds = float(input("Enter the amount of coffee for your order (in pounds): "))
    cost = (10.5 + .86) * pounds + 1.5
    print("The order will cost £", round(cost, 2), "in total.")

main()