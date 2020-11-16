# Chapter 11, programming exercise 11
# This is an automated censor program that 
# replaces all four-letter words by "****".

def fourLetters(word):
    count = 0
    for letter in word: 
        if letter.isalpha():
            count += 1
    if count == 4:
        return True
    return False

def censor(word):
    for i in range(len(word)):
        if word[i].isalpha():
            word = word[:i] + "*" + word[i+1:]
    return word

def main():
    print("\nThis is an automated censor program that will replace \n all four-letter words in a file with '****'.\n")
    filename = input("Enter the name of the data file to censor: ")
    text = open(filename, "r")

    censoredText = " "
    for line in text:
        words = line.split()
        for i in range(len(words)):
            if fourLetters(words[i]):
                words[i] = censor(words[i])
            censoredText += " ".join(words) + "\n"

    text.close()
    newFile = open("censored version" + filename, "w")
    newFile.write(censoredText)
    newFile.close()

if __name__ == '__main__':
    main()
