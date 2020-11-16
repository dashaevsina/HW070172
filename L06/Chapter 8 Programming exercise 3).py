# Chapter 8, programming exercise 3
# This program calculates how long it takes
# for an investment to double at a given 
# interest rate.

def main():
    print("This program will calculate how long it akes \n for an inverstment to double at a given \n interest rate.\n")
    annualisedInterestRate = float(input("Enter the annualised interest rate: "))
    principal = 1
    years = 0
    interest = principal

    while interest < principal * 2:
        interest = interest + interest * ((float(annualisedInterestRate)/100))
        years = years + 1
    partYear = interest % 2

    print("It will take %0.2f years for the investment to double in value." % (years-partYear))

main()