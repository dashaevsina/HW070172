# Chapter 6, programming exercise 2
# This program will print the lyrics 
# of the first 10 verses of 'The Ants
# Go Marching'.


def ants():

    number = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
    rhyme = ["suck his thumb", "tie his shoe", "ride a bee", "ask for more", "jump and dive", "pick up sticks", "play with a hen", " rollerskate", "drink and dine", " shout 'The End!'"]

    for i in range(10):
        print("The ants go marching {0} by {0}, hurrah! hurrah!".format(str(number[i])))
        print("The ants go marching {0} by {0}, hurrah! hurrah!".format(str(number[i])))
        print("The ants go marching {0} by {0}".format(str(number[i])))
        print("The little one stops to {0},".format(str(rhyme[i])))
        print("And they all go marching down... \n In the ground... \n To get out... \n Of the rain. \n Boom! Boom! Boom!")
        print()

def main():
        ants()
main()