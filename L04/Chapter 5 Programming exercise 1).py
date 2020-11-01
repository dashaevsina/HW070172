# Chapter 5, programming exercise 1
# dateconvert2.py
# This program converts the date 
# (in day, month and year) into 
# two possible date formats.

def main():
    day = int(input("Enter the day (in numabers): "))
    month = int(input("Enter the month (in numbers): "))
    year = int(input("Enter the year (in numbers): "))

    date1 = str(month)+"/"+str(day)+"/"+str(year)

    months = ["January", "February", "March", "April", 
            "May", "June", "July", "August", 
            "September", "October", "November", "December"]
    monthStr = months[month-1]

    date2 = monthStr+ " " + str(day) + ", " + str(year)

    print("The date that you entered is {0} or {1}.".format(date1, date2))

main()