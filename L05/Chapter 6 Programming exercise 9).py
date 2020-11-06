# Chapter 6, programming exercise 9
# This program converts a quiz score 
# to the corresponding grade.

def grade(score):
    grade = []
    for i in range (0, 60):
        grade.append("F")
    for i in range (60, 69):
        grade.append("D")
    for i in range (70, 79):
        grade.append("C")
    for i in range (80, 89):
        grade.append("B")
    for i in range (90, 100):
        grade.append("A")
    return grade[score]

def main():
    exam_score = int(input("Enter the quiz score (in numbers): "))
    x = grade(exam_score)
    print("Your grade is", x, ".")

main()