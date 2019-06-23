import os

print(os.getcwd())
# exit(0)

students = []


def add_student(sname):
    student = {"name": sname}
    students.append(student)


def save_file(student):
    try:
        file = open("student123.txt", "a")  # a is for append - access modes
        file.write(student + "\n")
        file.close()
        print("File saved")
    except Exception:
        print("Could not save the file")


def read_file():
    try:
        f = open("student123.txt", "r")
        for student in read_students(f):
            students.append(student)
        f.close()
        print("TEST")
    except Exception:
        print("Unable to read the file ")


def read_students(file):
    print(file)
    for line in file:
        yield line


# save_file(name)
print("Before read_file()")
read_file()
print("after read_file")
print(students)
print("End of the function")

# Lambda
# this two functions are the same


def double(x):
    return x * 2


doubl_as = lambda x: x * 2

doubl_as(5) == 10

