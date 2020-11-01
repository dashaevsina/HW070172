# futval.py
# A program to compute the value of an investment
# carried n years into the future

def main():
    print("This program calculates the total")
    print("accumulated value of an n-year")
    print("investment with a certain fixed")
    print("amount every year.")
principal = eval(input("Enter the initial principal: "))
apr = eval(input("Enter the annual interest rate: "))
annualInvestment = eval(input("Enter the fixed annual investment amount: "))
years = eval(input("Enter the number of investment years: "))

for i in range(years):
    # This calculates the amount at the beginning of the year 
    principal = principal + annualInvestment
    # This is the added interest
    principal = principal * (1 + apr)


    print("The value in ", years , "years is: ", principal)

main()