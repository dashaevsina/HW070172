# futval.py
# A program to compute the value of an investment
# carried n years into the future

def main():
    print("This program calculates the future value")
    print("of an n-year investment by describing")
    print("the interested accrued based on a")
    print("nominal rate and the number ofcompounding periods.")

principal = eval(input("Enter the initial principal: "))
rate = eval(input("Enter the annual interest rate: "))
periods = eval(input("Enter the number of times the interest is compounded each year: "))

for i in range(10 * periods):
    principal = principal * (1 + rate / periods)

    print("The value in 10 years is: ", principal)

main()