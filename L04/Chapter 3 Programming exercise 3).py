# Chapter 3, Programming exercise 3
# This program calculates the molecular 
# weight of a carbohydrate based on the 
# number of carbon and oxygen atoms.

import math 

def main():
    print("This program will calculate the molecular \n weight of a carbohydrate based on the \n number of carbon and oxygen atoms.")
    hydrogen = int(input("Enter the number of hydrogen atoms in the molecule: "))
    carbon = int(input("Enter the number of carbon atoms in the molecule: "))
    oxygen = int(input("Enter the numnber of oxygen atoms in the molecule: "))
    molecular_weight = hydrogen * 1.0079 + carbon * 12.011 + oxygen * 15.9994
    print("The molecular weight of the carbohydrate is", molecular_weight, "g/mol.")

main()