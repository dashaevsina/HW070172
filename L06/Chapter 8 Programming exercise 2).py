# Chapter 8, programming exercise 2
# This program prints a table of windchill
# values for the National Weather Service.

def windchillIndex(temperature, windSpeed):
    if 50 >= windSpeed >= 3:
        windchillIndex = 35.74 + 0.6215 * temperature - (35.75 * (windSpeed ** 0.16)) + (0.4275 * temperature) * (windSpeed ** 0.16)
    else:
        windchillIndex = 0
    return windchillIndex

def main():
    print("This program prints a table of windchill values.\n")
    print("{0:>11} {1:6} {2:6} {3:6} {4:6} {5:6} {6:6} {7:6} {8:6}".format(-20, -10, 0, 10, 20, 30, 40, 50, 60))
    print()
    for i in range(11):
        print("{0:2} {1:8.1f} {2:6.1f} {3:6.1f} {4:6.1f} {5:6.1f} {6:6.1f} {7:6.1f} {8:6.1f} {9:6.1f}".format(i*5,windchillIndex(-20, i*5), windchillIndex(-10, i*5), windchillIndex(0, i*5), windchillIndex(10, i*5), windchillIndex(20, i*5), windchillIndex(30, i*5), windchillIndex(40, i*5), windchillIndex(50, i*5), windchillIndex(60, i*5)))

main()