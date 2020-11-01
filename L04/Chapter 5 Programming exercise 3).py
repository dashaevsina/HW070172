# Chapter 5, programming exercise 3
# This program converts a quiz score 
# to the corresponding grade.

def main():
    exam_score = int(input("Enter the quiz score (in numbers):"))

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

    print("Your grade is", grade[exam_score], ".")

main()