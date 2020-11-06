# Chapter 7, programming exercise 6
# This program calculates speeding ticket fines. 

def BMI(weight, height):
    BMI = (weight * 720) / (height ** 2)
    return BMI

def main():
    print("This program will calculate speeding ticket fines (if applicable). \n")
    try: 
        speedLimit = int(input("Enter the speed limit: "))
        clockedSpeed = int(input("Enter the clocked speed: "))
    except NameError:
            print("Please enter a valid weight and height.")
    except TypeError:
            print("Please enter a valid weight and height.")
    except ValueError:
            print("Please enter a valid weight and height.")

    if clockedSpeed <= speedLimit:
        print("You were driving within the speed limit.")
    else:
        print("You were going above the speed limit.")
        if clockedSpeed > 90:
            fineAmount = 5 * (clockedSpeed - speedLimit) + 50 + 200
        else:
            fineAmount = 5 * (clockedSpeed - speedLimit) + 50
        print("The fine is €{0:.2f}.".format(fineAmount))

if __name__ == '__main__':
    main()