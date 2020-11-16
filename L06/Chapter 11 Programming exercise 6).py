# Chapter 11, programming exercise 6
# This program scrambles a list into 
# random order, like shuffling a deck 
# of cards.

from random import random

def shuffle(myList):
    newList = []
    for i in range(len(myList)):
        x = int(random() * len(myList)) 
        newList.append(myList[x])
        myList.remove(myList[x])
    return newList

def main():
    print("\nThis program will scramble a list into random order, \n like shuffling a deck of cards.\n")
    myList = input("Enter a series of whole numbers (separated by commas): ")
    myList = myList.split(",")
    for i in range(len(myList)):
        myList[i] = eval(myList[i])

    print("The shuffled list is", shuffle(myList), ".")

if __name__ == '__main__':
    main()