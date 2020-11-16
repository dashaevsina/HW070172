# Chapter 11, programming exercise 5
# This program creates a suitable function for
# a variety of algorithms.

# a) count(myList, x) (like myList.count(x))
def count(myList, x):
    total = 0
    for i in myList:
        if i == x:
            total = total + 1
    return total

# b) isin(myList, x) (like x in MyList))
def isin(myList, x):
    for i in myList:
        if i == x:
            return True

# c) index(myList, x) (like myList.index(x))
def index(myList, x):
    for i in range (len(myList)):
        if myList[i] == x:
            return i

# d) reverse(myList) (like myList.reverse())
def reverse(myList):
    return myList[-1: :-1]

# e) sort(myList) (like myList.sort())-- sorts in descending order
def sort(myList):
    newList = []
    for i in range(len(myList)):
        x = max(myList)
        newList.append(x)
        myList.remove(x)
    return newList

def main():
    print("\nThis program will create a suitable function for a variety of algorithms.\n")
    myList = input("Enter a series of whole numbers (separated by commas): ")
    myList = myList.split(",")
    for i in range(len(myList)):
        myList[i] = eval(myList[i])
    x = int(input("Enter the value x: "))

    print("The count of x is", count(myList, x), ".")
    print("The x in myList is", isin(myList, x), ".")
    print("The index of x is", index(myList, x), ".")
    print("The reverse of myList is", reverse(myList), ".")
    print("The sorted list in descending order is", sort(myList), ".")

if __name__ == '__main__':
    main()