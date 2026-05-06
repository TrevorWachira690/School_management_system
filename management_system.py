# ---------------- DATABASE ----------------


students_dictionary = {
    "form1": {
        {"Name": "John", "Admission_number": 5800, "Grade": None},
        {"Name": "Mary", "Admission_number": 5801, "Grade": None},
        {"Name": "Alice", "Admission_number": 5802, "Grade": None},
        {"Name": "Bob", "Admission_number": 5803, "Grade": None},
    },
    "form2": {
        {"Name": "Charlie", "Admission_number": 5804, "Grade": None},
        {"Name": "Diana", "Admission_number": 5805, "Grade": None},
        {"Name": "Eve", "Admission_number": 5806, "Grade": None},
        {"Name": "Frank", "Admission_number": 5807, "Grade": None}
    },
    "form3": {
        {"Name": "Grace", "Admission_number": 5808, "Grade": None},
        {"Name": "Heidi", "Admission_number": 5809, "Grade": None},
        {"Name": "Ivan", "Admission_number": 5810, "Grade": None},
        {"Name": "Judy", "Admission_number": 5811, "Grade": None}
    },
    "form4": {
        {"Name": "Trevor", "Admission_number": 5812, "Grade": None},
        {"Name": "Leo", "Admission_number": 5813, "Grade": None},
        {"Name": "Mallory", "Admission_number": 5814, "Grade": None},
        {"Name": "Nina", "Admission_number": 5815, "Grade": None}
    }
}

# ---------------- FUNCTION ----------------
def calculate_mean_score():
    Compulsories = {
        "Maths": int(input("Enter your Maths score: ")),
        "English": int(input("Enter your English score: ")),
        "Kiswahili": int(input("Enter your Kiswahili score: "))
    }

    Sciences = {
        "Physics": int(input("Enter your Physics score: ")),
        "Chemistry": int(input("Enter your Chemistry score: ")),
        "Biology": int(input("Enter your Biology score: "))
    }

    Technicals = {
        "Agriculture": int(input("Enter your Agriculture score: ")),
        "Computer": int(input("Enter your Computer score: ")),
        "Business": int(input("Enter your Business score: "))
    }

    Humanities = {
        "History": int(input("Enter your History score: ")),
        "Geography": int(input("Enter your Geography score: ")),
        "CRE": int(input("Enter your CRE score: "))
    }

    total = (
        sum(Compulsories.values()) +
        sum(Sciences.values()) +
        sum(Technicals.values()) +
        sum(Humanities.values())
    )

    mean_score = round(total / 8)
    print(f"Your mean score is: {mean_score}")

    if mean_score >= 80: return "A"
    elif mean_score >= 75: return "A-"
    elif mean_score >= 70: return "B+"
    elif mean_score >= 65: return "B"
    elif mean_score >= 60: return "B-"
    elif mean_score >= 50: return "C+"
    elif mean_score >= 40: return "C"
    elif mean_score >= 30: return "C-"
    elif mean_score >= 20: return "D+"
    elif mean_score >= 10: return "D"
    else: return "F"


# ---------------- MAIN PROGRAM ----------------
confirmation = int(input("Hello! Welcome to the student management system. What do you want to do today? \n(1: Add a new student, 2: Calculate student grade): "))
if confirmation == 1:
    # Input new student details
    Name = input("Enter the name of the new student: ").strip()
    Admission_number = int(input("Enter the admission number of the new student: "))
    Class = input("Enter the class of the new student: ").lower().replace(" ", "")

    # Check if all inputs are provided
    if Name and Admission_number and Class:

        if Class in students_dictionary:

            # Check if student already exists
            if Name in students_dictionary[Class]:
                print("Error: Student already exists in this class!")

            else:
                # Add new student
                students_dictionary[Class][Name] = {
                    "Admission_number": Admission_number,
                    "Grade": None
                }
                print(f"Student {Name} added successfully to {Class}.")

        else:
            print("Error: Invalid class!")

elif confirmation == 2:
    number = int(input("Enter your admission number: "))
    student_class = input("Enter your class: ").lower().replace(" ", "")

    # Validate class first
    if student_class not in students_dictionary:
        print("Error: Invalid class!")
    else:
        # Find student by admission number
        found = False

        for name, details in students_dictionary[student_class].items():
            if details["Admission_number"] == number:
                found = True

                grade = calculate_mean_score()
                students_dictionary[student_class][name]["Grade"] = grade

                # Feedback
                print(f"\nHello, {name}!")

                if grade == "A":
                    print("You're doing wonderfully")
                elif grade == "A-":
                    print("You're doing so nicely")
                elif grade == "B+":
                    print("You're getting there")
                elif grade == "B":
                    print("You can do better")
                elif grade == "B-":
                    print("You need to work harder")
                elif grade == "C+":
                    print("You're passing")
                elif grade == "C":
                    print("You can do better")
                elif grade == "C-":
                    print("You need to work harder")
                elif grade == "D+":
                    print("You're doing okay")
                elif grade == "D":
                    print("You need to improve")
                else:
                    print("You failed")

                print("\nClass Logbook:")
                print(students_dictionary[student_class][name])

        if not found:
            print("Error: Admission number not found!")

else:
    print("Error: Invalid option selected!")