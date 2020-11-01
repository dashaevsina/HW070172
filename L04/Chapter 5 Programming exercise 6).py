# Chapter 5, programming exercise 6
# This program calculates the numeric
# value of a complete name.

def main():
    print("This program will calculate the numeric value \n of a full name.")
    name = input("Enter your full name here (separated by spaces): ")
    
    fullName = "".join(name)
    fullName = fullName.lower()
    fullName = fullName.lstrip()
    fullName = fullName.replace("-", "`")
    fullName = fullName.replace(" ", "`")

    x = 0
    for chr in fullName:
        x = int(ord(chr)) + x - 96
    
    print("The numeric value of your full name is {0}.".format(x))

main()
