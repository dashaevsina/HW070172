# Chapter 7, programming exercise 1
# This program calculates the total wages 
# for the week based on the number of 
# hours worked and the hourly rate.

def main():
    print("This program will calculate the total wages for the week.\n")
    numberOfHoursWorked = 0
    if numberOfHoursWorked <= 0:
        try:
            numberOfHoursWorked = float(input("Enter the number of hours worked: "))
            hourlyRate = float(input("Enter the hourly wage: "))
        except NameError:
            print("Please enter a valid number.")
        except TypeError:
            print("Please enter a valid number.")
        except SyntaxError:
            print("Please enter a valid number.")

    if numberOfHoursWorked <= 40:
        salary = numberOfHoursWorked * hourlyRate
    else:
        salary = 40 * salary + (numberOfHoursWorked - 40) * 1.5 * salary
    print("Your weekly salary is €", salary, ".")

if __name__ == '__main__':
    main()