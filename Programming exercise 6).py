# futval.py
# A program to compute the value of an investment
# carried n years into the future

def main():
    print("This program calculates the future value")
    print("of an n-year investment.")
principal = eval(input("Enter the initial principal: "))
apr = eval(input("Enter the annual interest rate: "))
years = eval(input("Enter the number of investment years: "))

for i in range(years):
    principal = principal * (1 + apr)

    print("The value in ", years, "years is", principal)

main()