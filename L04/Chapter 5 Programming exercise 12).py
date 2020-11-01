# Chapter 5, programming exercise 12
# This is an improved version of the 
# futval.py program from Chapter 2.

def main():
    print("This program calculates the future value \n of a 10-year investment.")
    
    principal = int(input("Enter the initial principal: "))
    apr = eval(input("Enter the annual interest rate: "))

    print("{0:<9}{1:<7}".format("Year", "Value"))
    print("--------------------------")

    for i in range (10):
        principal = principal * (1 + .01 * apr)
    
    print("{0:>2}       ${1:<}.{2:0^2}".format(i+1, int(principal), int(principal %1 * 100)))
main()