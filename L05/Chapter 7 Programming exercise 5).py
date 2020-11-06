# Chapter 7, programming exercise 5
# This program calculates a person's BMI. 

def BMI(weight, height):
    BMI = (weight * 720) / (height ** 2)
    return BMI

def main():
    print("This program will calculate a person's BMI. \n")
    try: 
        weight = float(input("Enter the weight (in pounds): "))
        height = float(input("Enter the height (in inches): "))
        bmi = BMI(weight, height)
    except NameError:
            print("Please enter a valid weight and height.")
    except TypeError:
            print("Please enter a valid weight and height.")
    except ValueError:
            print("Please enter a valid weight and height.")

    if 19 <= bmi <= 25:
        print("You are in the healthy BMI range.")
    elif bmi < 19:
        print("You are in the underweight BMI range.")
    elif bmi > 25:
        print("You are in the overweight BMI range.")
    else:
        print("Please enter a valid weight (in pounds) and height (in inches).")

if __name__ == '__main__':
    main()