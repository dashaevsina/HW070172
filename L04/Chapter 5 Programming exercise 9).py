# Chapter 5, programming exercise 9
# This program counts the number of 
# words in a sentence.

def main():
    sentence = input("Enter your sentence here: ")

    word_length = []

    for string in sentence.split():
        x = string[0]
        word_length.append(x)

    print("The number of words in your sentence is:", (len(word_length)), ".")

main()