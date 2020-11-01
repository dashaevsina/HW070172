# Chapter 5, programming exercise 2
# This program converts a quiz score 
# to the corresponding grade.

def main():
    exam_score = int(input("Enter the quiz score (from 0 to 5):"))

    grade = ["F", "F", "D", "C", "B", "A"]

    print("Your grade is", grade[exam_score])

main()