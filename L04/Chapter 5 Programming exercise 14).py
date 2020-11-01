# Chapter 5, programming exercise 13
# This is a program that analysis a
# file to determien the number of 
# lines, words, and cahracters contained
# therein.  

def main():
    print("This program will access a file and calculate the total \n number of lines, words, and \n characters contained therein.")
    fname = input("Enter filename: ")

    infile = open(fname, "r")
    fileLines = infile.readlines()

    lines = []
    for line in fileLines:
        lines.append(line)
    print ("In the file", fname, "the number of lines is {0}.".format(len(lines)))
    infile.close()

    infile = open(fname, "r")
    data = infile.read()

    numberOfWords = []
    for string in data.split():
        x = string[0]
        numberOfWords.append(x)

    numberOfCharacters = []
    for string in data.split():
        x = string[0]
        numberOfCharacters.append(x)
    infile.close()

    print("The number of words in the file", fname, "is {0}".format(len(numberOfWords)), ".")
    print("The total number of characters in the file", fname, "is {0}".format(numberOfCharacters), ".")

    
main()