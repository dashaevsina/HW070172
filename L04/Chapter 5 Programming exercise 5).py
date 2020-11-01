# Chapter 5, programming exercise 5
# This program calculates the numeric
# value of a single name.

def main():
    print("This program will calculate the numeric value \n of a name.")
    name = input("Enter your name here: ")
    
    name = name.lower()

    x = 0
    for chr in name:
        x = int(ord(chr)) + x - 96
    
    print("The numeric value of your name is {0}.".format(x))

main()
