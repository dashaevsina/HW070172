# Chapter 7, programming exercise 3
# This program calculates the corresponding 
# grade of an exam score. 

def main():
    print("This program will calculate the corresponding grade of an exam score.\n")
    try:
        examScore = int(input("Enter your exam score: "))
    except NameError:
            print("Please enter a valid number between 0 and 100.")
    except TypeError:
            print("Please enter a valid number between 0 and 100.")
    except ValueError:
            print("Please enter a valid number between 0 and 100.") 


    if 100 > examScore >= 90:
        grade = "A"
    elif 90 > examScore  >= 80:
        grade = "B"
    elif 80 > examScore >= 70:
        grade = "C"
    elif 70 > examScore >= 60:
        grade = "D"
    elif 60 > examScore:
        grade = "F"
    else:
        print("Please enter a valid number between 0 and 100.")
        

    print("The corresponding grade of your exam score is ", grade, ".")

if __name__ == '__main__':
    main()