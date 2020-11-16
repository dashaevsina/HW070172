# Chapter 8, programming exercise 4
# This program prints the Syracuse  
# sequence for a specific starting value. 

def main():
    print("This program will print the Syracuse sequence for a specific starting value.\n")
    startingValue = int(input("Enter a number to use as the starting value: "))

    print("The Syracuse sequence for your starting value", startingValue, "is: ", str(startingValue) + ", ", end="")
    while startingValue != 1:
        if startingValue % 2 == 0:
            startingValue = startingValue // 2
        else:
            startingValue = 3 * startingValue + 1
        
        if startingValue != 1:
            print(str(startingValue) + ", ", end="")
        else: 
            print(1)
    
main()