# Chapter 11, programming exercise 8
# This program removes duplicate values 
# from a list. 

def removeDuplicates(somelist):
    newList = []
    for elem in somelist:
        if elem not in newList:
            newList.append(elem)
    somelist[:] = newList

def main():
    print("\nThis program will remove duplicate values from a given list.\n")
    somelist = [12, 465, 33, 78, 12, 31, 13, 27, 45, 27, 62, 99]
    print("The initial list was", somelist, ".\n")
    
    removeDuplicates(somelist)
    
    print("The duplicate values have been removed from the list.\n The new list is: ", somelist, ".")

if __name__ == '__main__':
    main()