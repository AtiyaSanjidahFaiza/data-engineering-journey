students = {
    "Atiya": 85,
    "Faiza": 90,
    "Rahim": 78
}

print("Student Marks")
for name, marks in students.items():
    print(name, ":", marks)

name = input("Enter student name: ")

if name in students:

    print(name, students[name])
else:
    print("Student not found.")
#phonebook
phonebook = {
    "atiya": "01911111111",
    "sanjidah": "01777777777",
    "faiza": "0181111111"
}

print("Phone Book")
for name, phone in phonebook.items():
    print(name, ":", phone)

search = input("Enter a name: ")

if search in phonebook:
    print(search, ":", phonebook[search])
else:
    print("Contact not found.")
#word counter
text= input("enter a sentence")
words = text.split()
count= len(words)
print(count)