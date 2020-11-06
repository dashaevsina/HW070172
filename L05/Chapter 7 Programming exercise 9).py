# Chapter 7, programming exercise 9
# This program calculates the date of 
# Easter in the years 1982-2048 inclusive.

def dateOfEaster(year):
    if 1982 <= year <= 2048:
        a = year % 19
        b = year % 4
        c = year % 7
        d = (19 * a + 24) % 30
        e = (2 * b + 4 * c + 6 * d + 5) % 7
        if ( d + e ) > 9:
            print("Easter falls on April {}.".format(d + e -9))
        else:
            print("Easter falls on March {}.".format(22 + d + e))
    else:
        print("The specified year is not in the proper range.")

def main():
    print("This program will calculate the date of Easter in the years \n 1982- 2048 inclusive.")

    try:
        year = int(input("Enter a year (from 1982 to 2048): "))
    
    except NameError:
            print("Please enter a valid year in the yyyy format.")
    except TypeError:
            print("Please enter a valid year in the yyyy format.")
    except ValueError:
            print("Please enter a valid year in the yyyy format.")

    dateOfEaster(year)


if __name__ == '__main__':
    main()