# convert.py
# A program to convert temperatures from Fahrenheit to Celsius

def main():
    fahrenheit = eval(input("What is the Fahrenheit temperature? "))
    celsius = (fahrenheit - 32) * 5/9
    print ("The temperature is", celsius, "degrees Celsius")
main()