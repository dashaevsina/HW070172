# Chapter 7, programming exercise 2
# This program calculates the corresponding 
# grade of a quiz score. 

def main():
    print("This program will calculate the corresponding grade of a quiz score.\n")
    try:
        quizScore = int(input("Enter your quiz score: "))
    except NameError:
            print("Please enter a valid number between 0 and 5.")
    except TypeError:
            print("Please enter a valid number between 0 and 5.")
    except ValueError:
            print("Please enter a valid number between 0 and 5.") 


    if quizScore == 5:
        grade = "A"
    elif quizScore == 4:
        grade = "B"
    elif quizScore == 3:
        grade = "C"
    elif quizScore == 2:
        grade = "D"
    elif quizScore == 1:
        grade = "F"
    elif quizScore == 0:
        grade = "F"
    else:
        print("Please enter a valid number between 0 and 5.")
        

    print("The grade for your quiz is ", grade, ".")

if __name__ == '__main__':
    main()