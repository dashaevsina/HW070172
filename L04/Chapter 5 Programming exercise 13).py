# Chapter 5, programming exercise 13
# This is an improved version of a
# previous programming problem to make
# it batch-oriented. 

def main():
    print("This program will access a file and calculate the total \n number of letters, words, and \n the average word length.")
    fname = input("Enter filename: ")
    infile = open(fname, "r")
    data = infile.read()

    numberOfWords = []

    for string in data.split():
        x = string[0]
        numberOfWords.append(x)

    letterTotal = 0
    for string in data.split():
        letterTotal = len(string) + letterTotal
        wordAverage = letterTotal / (len(numberOfWords))

        infile.close()

    print("The number of words in the file", fname, "is {0}".format(len(numberOfWords)), ".")
    print("The total number of letters in the file", fname, "is {0}".format(letterTotal), ".")
    print("The average word length in the file", fname, "is {0}".format(wordAverage), ".")

    
main()