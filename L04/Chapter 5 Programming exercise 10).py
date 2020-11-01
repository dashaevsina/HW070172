# Chapter 5, programming exercise 10
# This program counts the average word
# length in a sentence.

def main():
    sentence = input("Enter your sentence here: ")

    numberOfWords = []

    for string in sentence.split():
        x = string[0]
        numberOfWords.append(x)

    letTotal = 0
    for string in sentence.split():
        letTotal = len(string) + letTotal
        wordAverage = letTotal / (len(numberOfWords))

    print("The average word length in your sentence is:", wordAverage, ".")

main()