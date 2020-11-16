# Chapter 11, programming exercise 4
# This program with a GUI sorts a file of students 
# based on GPA, name, or credits. 

from gpa import student

def makeStudent(informationOnStudent):
    name, hours, qpoints = informationOnStudent.split("\t")
    return student(name, hours, qpoints)

def readStudents(filename):
    infile = open(filename, "r")
    students = []
    for line in infile:
        students.append(makeStudent(line))
    infile.close()
    return students

def writeStudents(students, filename):
    # students is a list of Student objects
    outfile = open(filename, "w")
    for s in students:
        print("{0}\t{1}\t{2}".format(s.getName(), s.getHours(), s.getQPoints()), file=outfile)
        outfile.close()

def main():
    print("This program sorts student grade information by name, hours or GPA.\n")
    filename = input("Enter the name of the data file: ")
    data = readStudents(filename)

    while True:
        sortingField = (input("Type either 'GPA', 'name' or 'credits' to sort the file of students: "))
        ascendingOrDescending = (input("Type 'ascending' to view the files in ascending order and \n type 'descending' for descending order: "))
        if sortingField == "GPA":
            data.sort(key=student.gpa)
            if ascendingOrDescending == "descending":
                data.reverse()
            break
        elif sortingField == "name":
            data.sort(key=student.getName)
            if ascendingOrDescending == "descending":
                data.reverse()
            break
        elif sortingField == "credits":
            data.sort(key=student.getQPoints)
            if ascendingOrDescending == "descending":
                data.reverse()
            break
        else:
            print("Please enter a valid category for sorting the file.")

    filename = input("Enter a name for the output file: ")
    writeStudents(data, filename)
    if ascendingOrDescending == "descending":
        print("The data has been written in descending order to", filename, ".")
    else:
        print("The data has been written in ascending order to", filename, ".")

if __name__ == '__main__':
    main()