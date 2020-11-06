# Chapter 6, programming exercise 1
# This program will print the lyrics 
# of the song 'Old MacDonald' for 5 
# different animals.


def oldMacDonald():
    print("Old MacDonald had a farm, Ee-igh, Ee-igh, Oh!")

def animal(animal, sound):
        print("And on that farm he had a", animal, "Ee-igh, Ee-igh, Oh!")
        print("With a", sound, "here and a", sound, "there.")
        print("Here a", sound, "there a", sound, "everywhere a", sound,".")

def main():
        oldMacDonald()
        animal("cow", "moo moo")
        oldMacDonald()
        print()
        oldMacDonald()
        animal("dog", "bow-wow")
        oldMacDonald()
        print()
        oldMacDonald()
        animal("hen", "cluck-cluck")
        oldMacDonald()
        print()
        oldMacDonald()
        animal("goat", "meh meh")
        oldMacDonald()
        print()
        oldMacDonald()
        animal("sheep", "baa baa")
        oldMacDonald()

main()



