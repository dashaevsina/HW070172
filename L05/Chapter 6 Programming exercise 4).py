# Chapter 6, programming exercise 4
# This program  caclulates the sum 
# and the sum of the cubes of the first 
# n natural numbers.


def sumN(n):
    number = 1
    for factor in range(n, 1, -1):
        number = number + factor
    return number

def sumNCubes(n):
    cube = 1
    for factor in range(n, 1, -1):
        cube = cube + factor ** 3
    return cube

def main():
    print("This program will calculate the sum and the sum of the cubes of the first n natural numbers.")
    n = int(input("Enter a value: "))
    N = sumN(n)
    NCubes = sumNCubes(n)
    print("The sum of the first {0} natural numbers is {1}, and the sum of the \n first {0} cubes is {2}".format(n, N, NCubes), ".")


main()