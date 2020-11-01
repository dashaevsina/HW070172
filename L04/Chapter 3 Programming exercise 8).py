# Chapter 3, Programming exercise 8
# This program calculates the Gregorian  
# epact (the number of days between
# January 1st and the previous new moon).

import math

def main():
    print("This program calculates the Gregorian epact.")
    year = int(input("Please enter the 4-digit year: "))
    C = year // 100
    epact = (8 + (C // 4) - C + ((8 * C + 13) // 25) + 11 * (year % 19)) % 30
    print("The Gregorian epact is", epact, ".")

main()