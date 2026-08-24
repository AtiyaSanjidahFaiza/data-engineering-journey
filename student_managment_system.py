import json

file_name = "Coaching.json"

def load_stud():
    try:
        with open(file_name, "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        print("error reading file")
        return []


# CHANGED: added information_of_customers parameter
def save_info(information_of_customers):
    try:
        with open(file_name, "w") as file:
            json.dump(information_of_customers, file, indent=4)

    except Exception as e:
        print("Error saving file", e)


def add_info(information_of_customers):
    stud_name = input("Enter student name: ")
    stud_father_name = input("Enter Father name: ")
    stud_mother_name = input("Enter Mother name: ")
    address = input("Address: ")
    email = input("Email: ")

    try:
        id = int(input("Enter student Id: "))
        sphone = int(input("Enter Phone number: "))
        fphone = int(input("Enter Father Phone number: "))
        mphone = int(input("Enter mother Phone number: "))
        sclass = int(input("Enter class: "))
        absent = int(input("Absent: "))
        present = int(input("Present: "))

        information = {
            "student_name": stud_name,
            "father_name": stud_father_name,
            "mother_name": stud_mother_name,
            "address": address,
            "email": email,
            "id": id,
            "student_phone": sphone,
            "father_phone": fphone,
            "mother_phone": mphone,
            "class": sclass,
            "absent": absent,
            "present": present
        }

        information_of_customers.append(information)

        save_info(information_of_customers)

        print("added successfully!")

    except ValueError:
        print("Invalid value. Enter correctly.")


def view_info(information_of_customers):

 if len(information_of_customers) == 0:
        print("No student found!")
        return
 else:
    for information in information_of_customers:
        print("Student Name:", information["student_name"])
        print("Father Name:", information["father_name"])
        print("Mother Name:", information["mother_name"])
        print("Address:", information["address"])
        print("Email:", information["email"])
        print("Student ID:", information["id"])
        print("Student Phone:", information["student_phone"])
        print("Father Phone:", information["father_phone"])
        print("Mother Phone:", information["mother_phone"])
        print("Class:", information["class"])
        print("Absent:", information["absent"])
        print("Present:", information["present"])


def seacrh_info(information_of_customers):

    try:
        id = int(input("Enter student Id: "))

        for information in information_of_customers:

            # CHANGED: information[id] → information["id"]
            if information["id"] == id:
                print("Name:", information["student_name"])
                print("Father Name:", information["father_name"])
                print("Mother Name:", information["mother_name"])
                print("Address:", information["address"])
                print("Email:", information["email"])
                print("Student ID:", information["id"])
                print("Student Phone:", information["student_phone"])
                print("Father Phone:", information["father_phone"])
                print("Mother Phone:", information["mother_phone"])
                print("Class:", information["class"])
                print("Absent:", information["absent"])
                print("Present:", information["present"])
                return

        # CHANGED: moved outside the loop
        print("Student not found")

    except ValueError:
        print("Invalid ID")


def delete_info(information_of_customers):

    try:
        id = int(input("Enter student Id: "))

        for information in information_of_customers:

            # CHANGED: information[id] → information["id"]
            if information["id"] == id:
                information_of_customers.remove(information)

                save_info(information_of_customers)

                print("Deleted Successfully!")
                return

        # CHANGED: moved outside the loop
        print("Student not found")

    except ValueError:
        print("Invalid ID")


def main():

    information_of_customers = load_stud()

    while True:

        print("1. Add student")
        print("2. view student")
        print("3. search student")
        print("4. Delete student")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                add_info(information_of_customers)

            elif choice == 2:
                view_info(information_of_customers)

            elif choice == 3:
                seacrh_info(information_of_customers)

            elif choice == 4:
                delete_info(information_of_customers)

            elif choice == 5:
                print("Exit")

                # CHANGED: added break
                break

            else:
                print("invalid choice")

        except ValueError:
            print("enter a number")


main()