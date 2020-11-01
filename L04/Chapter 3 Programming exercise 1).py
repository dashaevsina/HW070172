# Chapter 3, programming exercise 1
# This program calculates the volume 
# and surface area of a sphere

import math 

def main():
    print("This program will calculate the volume \n and surface area of a sphere")
    radius = int(input("Enter a value for the radius: "))
    volume = 4/3 * math.pi * (radius ** 3)
    area = 4 * math.pi * (radius ** 2)
    print("A sphere with a radius of ", radius, "has a volume of", round(volume, 2), "and a surface area of", round(area, 2), ".")

main()
