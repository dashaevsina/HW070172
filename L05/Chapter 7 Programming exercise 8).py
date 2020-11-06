# Chapter 7, programming exercise 8
# This program calculates eligibility
# for the US Senate and House.

def main():
    print("This program will calculate eligibility for the US Senate and House. \n")

    try:
        yearsOfCitizenship = float(input("Enter the years of citizenship: "))
        age = int(input("Enter your age: "))
    
    except NameError:
            print("Please enter a valid number.")
    except TypeError:
            print("Please enter a valid number.")
    except ValueError:
            print("Please enter a valid number.")

    if yearsOfCitizenship >= 9:
        if age >= 30:
            print("You are eligible to become a US Senator or a member of the House.")
        elif 30 > age >=25:
            print("You are eligible to become a US representative.")
        else:
            print("Sorry but you are too young to be eligible for the \n US Senate and House.")
    elif yearsOfCitizenship >= 7 and age >= 25:
        print("You are eligible to become a US representative.")
    else:
            print("Sorry but you have not held US citizenship for the requisite \n amount of years and are therefore not eligible for the \n US Senate and House.")


if __name__ == '__main__':
    main()