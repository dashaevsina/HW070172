# Celsius and Fahrenheit table
# A program that produces a table of temperatures
# in Celsius and Fahrenheit for every 10 degrees
# from 0ºC to 100ºC

print("This program will generate a table of")
print("Celsius temperatures and the Fahrenheit")
print("equivalents every 10 degrees from 0ºC to 100ºC.")
print("                                               ")
def main():
    print("Celsius temperatures and Fahrenheit equivalents")
    print("Celsius", "                    ", "Fahrenheit")
    print("------------------------------------------------")

    degrees= [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    for celsius in degrees:
        print(celsius, "                        ", 9/5 * celsius + 32)

main()
