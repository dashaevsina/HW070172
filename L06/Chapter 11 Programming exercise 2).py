# Chapter 11, programming exercise 2
# This program sorts a file of students 
# based on GPA, name, or credits. 

from gpa import student

def makeStudent(informationOnStudent):
    name, hours, qpoints = informationOnStudent.split("\t")
    return Student(name, hours, qpoints)

def readStudents(filename):
    infile = open(filename, 'r')
    students = []
    for line in infile:
        students.append(makeStudent(line))
    infile.close()
    return students

def writeStudents(students, filename):
    # students is a list of Student objects
    outfile = open(filename, 'w')
    for s in students:
        print("{0}\t{1}\t{2}".format(s.getName(), s.getHours(), s.getQPoints()), file=outfile)
        outfile.close()

def main():
    print("This program sorts student grade information by name, hours or GPA.\n")
    filename = input("Enter the name of the data file: ")
    data = readStudents(filename)

    while True:
        sortingField = (input("Type either 'GPA', 'name' or 'credits' to sort the file of students: "))
        if sortingField == "GPA":
            data.sort(key=Student.gpa)
            break
        elif sortingField == "name":
            data.sort(key=Student.getName)
            break
        elif sortingField == "credits":
            data.sort(key=Student.getQPoints)
            break
        else:
            print("Please enter a valid category for sorting the file.")

    filename = input("Enter a name for the output file: ")
    writeStudents(data, filename)
    print("The data has been written to", filename, ".")

if __name__ == '__main__':
    main()