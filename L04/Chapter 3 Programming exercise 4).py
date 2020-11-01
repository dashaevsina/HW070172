# Chapter 3, Programming exercise 4
# This program calculates the distance to 
# a lightning strike based on the time
# elapsed between the flash and the sound 
# of thunder. 

import math

def main ():
    print("This program calculates the distance to \n a lightning strike based on the time \n between the flash and the sound \n of thunder.")
    time_elapsed = int(input("Enter the amount of time elapsed between the flash and the sound of thunder: "))
    miles = 1100 * time_elapsed / 5280
    print("The lightnight struck", miles, "miles away.")

main()
