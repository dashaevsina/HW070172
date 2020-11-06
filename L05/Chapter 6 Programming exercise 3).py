# Chapter 6, programming exercise 3
# This program caclulates the volume 
# and surface area of a sphere using
# functions.

import math

def sphereArea(radius):
    area = 4 * math.pi * (radius ** 2)
    return area

def sphereVolume(radius):
    volume = 4/3 * math.pi * (radius ** 3)
    return volume

def main():
    print("This program will calculate the volume and surface area of a sphere given the radius.")
    radius = float(input("Enter a value for the radius: "))
    area = sphereArea(radius)
    volume = sphereVolume(radius)
    print("A sphere with a radius of", radius, "has a volume of", round(volume, 2), "\nand a surface area of", round(area, 2),".")


main()