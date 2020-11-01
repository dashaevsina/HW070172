# Chapter 5, programming exercise 11
# This is an improved version of the 
# chaos.py program from Chapter 1.

def main():
    print("This program illustrates a chaotic function.")
    
    x = float(input("Enter a decimal number between 0 and 1: "))
    y = float(input("Enter another decimal number between 0 and 1: "))
    n = input("How many numbers should I print?")

    print("\n{0} {1:^8}         {2:^8}".format("index", x, y))
    print("-"*27)
    for i in n:
        x = 3.9 * x - 3.9 * x * x
        y = 3.9 * y - 3.9 * y * y
    
    print("{0:^5} {1:8.6f}     {2:8.6f}".format(i, x, y))
main()