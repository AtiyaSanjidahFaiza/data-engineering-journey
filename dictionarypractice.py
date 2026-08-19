students = {}
for i in range(5):
    id = input("enter student id: ")
    name = input("enter student name: ")
    dept = input("Enter department: ")
    phone = input("Enter mobile number: ")
    cgpa = input("enter CGPA: ")
    students[id] = {
        "name" : name,
        "department" : dept,
        "phone" : phone,
        "CGPA"  : cgpa
    }
print(students)