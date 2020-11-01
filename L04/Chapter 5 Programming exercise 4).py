# Chapter 5, programming exercise 4
# This program creates acronyms.

def main():
    print("This program will create an acronym of a given phrase.")
    phrase = str(input("Enter your phrase here (separated by spaces): "))
    list_of_words = phrase.split()

    acronym = " "
    for word in list_of_words:
        acronym += word[0].upper()

    print("The acronym of your phrase is", acronym + ".")

main()
