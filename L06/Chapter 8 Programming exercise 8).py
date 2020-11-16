# Chapter 8, programming exercise 8
# This program finds the greatest common 
# divisor (GCD) of two numbers using an 
# algorithm. 

def main():
    print("This program will find the greatest common divisor (GCD) of two numbers.\n")
    try:
        m = int(input("Enter a number: "))
        n = int(input("Enter another number: "))

    except NameError:
        print("\nPlease enter a valid number.\n")
    except TypeError:
        print("\nPlease enter a valid number.\n")
    except ValueError:
        print("\nPlease enter a valid number.\n") 
    
    if m < n:
        y = n
        n = m
        m = y

    while m != 0:
        y = m
        m = n % m
        n = y
    print("The GCD is {}".format(n), ".")



main()