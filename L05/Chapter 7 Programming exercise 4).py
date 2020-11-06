# Chapter 7, programming exercise 4
# This program calculates class standing
# according to the number of credits earned. 

def main():
    print("This program will calculate class standing from the number of credits earned. \n")
    try:
        numberOfCredits = int(input("Enter the number of credits earned: "))
    except NameError:
            print("Please enter a valid number.")
    except TypeError:
            print("Please enter a valid number.")
    except ValueError:
            print("Please enter a valid number.") 


    if numberOfCredits < 7:
        classStanding = "Freshman"
    elif 7 <= numberOfCredits < 16:
        classStanding = "Sophomore"
    elif 16 <= numberOfCredits < 26:
        classStanding = "Junior"
    elif numberOfCredits >= 26:
        classStanding = "Senior"
    else:
        print("Please enter a valid number.")
        

    print("Based on the number of credits, your class standing is", classStanding, ".")

if __name__ == '__main__':
    main()