# Chapter 7, programming exercise 7
# This program calculates the total 
# babysitting bill based on the starting 
# and ending times.

def timeToDecimals(timeString):
    hourString, minuteString = timeString.split(":")
    hour = int(hourString)
    minute = int(minuteString)
    return hour + minute / 60

def main():
    print("This program will calculate the total babysitting bill \n based on the starting and ending times. \n")

    rateBefore9pm = 2.5
    rateAfter9pm = 1.75

    try:
        start = input("Enter the starting time in the 24-hour format: ")
        startingTime = timeToDecimals(start)
        end = input("Enter the ending time in the 24-hour format: ")
        endingTime = timeToDecimals(end)

    except NameError:
            print("Please enter a valid time from 00:00 to 23:59.")
    except TypeError:
            print("Please enter a valid time from 00:00 to 23:59.")
    except ValueError:
            print("Please enter a valid time from 00:00 to 23:59.")

    if endingTime <21:
        bill = (endingTime - startingTime) * rateBefore9pm
    elif startingTime <21 and endingTime >= 21:
        bill =(21 - startingTime) * rateBefore9pm + (endingTime - 21) * rateAfter9pm
    else:
        bill = (endingTime - startingTime) * rateAfter9pm

    print("The total babysitting bill amounts to €{0:.2f}.".format(bill))

if __name__ == '__main__':
    main()