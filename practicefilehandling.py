lines = ["name  id  phone  department\n","Atiya 04 01811825500 CSE\n",
         "Sanjidah 05 01911111111 English\n",
         "Faiza 12 017111111111 Math\n",
         "Unaisa 15 0166666666, Microbiology\n",
         "Fareta 6 012222222222, BBA\n",
         "Ara 9 01555555555, HR\n"]
with open ("student.txt","w", encoding="utf 8") as student:
    student.writelines(lines)
with open ("student.txt","a", encoding="utf 8") as student:
    student.writelines("Nafisa 66 01666666666 BBA")
with open ("student.txt","r", encoding="utf 8") as student:
    print(student.read())
    count = len(lines)-1
print("total students = ", count)
search = input("Enter student name: ")
with open ("student.txt","r", encoding="utf 8") as student:
    for line in student:
        if search.lower() in line.lower():
            print("student found")
            print(line)
        