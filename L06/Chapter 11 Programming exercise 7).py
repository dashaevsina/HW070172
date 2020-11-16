# Chapter 11, programming exercise 7
# This program tests the function innerProd(x,y)
# that computes the inner product of two 
# (same length) lists.

def innerProd(x, y):
    sum = 0
    for (xi, yi) in zip(x, y):
        sum += xi * yi
    return sum

def main():
    print("\nThis program will compute the inner product of two (same length) lists.\n")
    myList = input("Enter a series of whole numbers (separated by commas): ")
    myList = myList.split(",")
    for i in range(len(myList)):
        myList[i] = eval(myList[i])
    anotherList = input("Enter another series of the same length \n (separate the whole numbers by commas): ")
    anotherList = anotherList.split(",")
    for i in range(len(anotherList)):
        anotherList[i] = eval(anotherList[i])

    list(zip([myList], [anotherList]))

    print("The inner product of the two (same length) lists is", innerProd(myList, anotherList), ".")

if __name__ == '__main__':
    main()