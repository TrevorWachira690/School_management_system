# ---------------- DATABASE ----------------

students_dictionary = {
    "form1": {
        "John": {"Admission_number": 5800, "Grade": None},
        "Mary": {"Admission_number": 5801, "Grade": None},
        "Alice": {"Admission_number": 5802, "Grade": None},
        "Bob": {"Admission_number": 5803, "Grade": None},
    },
    "form2": {
        "Charlie": {"Admission_number": 5804, "Grade": None},
        "Diana": {"Admission_number": 5805, "Grade": None},
        "Eve": {"Admission_number": 5806, "Grade": None},
        "Frank": {"Admission_number": 5807, "Grade": None}
    },
    "form3": {
        "Grace": {"Admission_number": 5808, "Grade": None},
        "Heidi": {"Admission_number": 5809, "Grade": None},
        "Ivan": {"Admission_number": 5810, "Grade": None},
        "Judy": {"Admission_number": 5811, "Grade": None}
    },
    "form4": {
        "Trevor": {"Admission_number": 5812, "Grade": None},
        "Leo": {"Admission_number": 5813, "Grade": None},
        "Mallory": {"Admission_number": 5814, "Grade": None},
        "Nina": {"Admission_number": 5815, "Grade": None}
    }
}

# ---------------- FUNCTION ----------------
def calculate_mean_score():
    try:
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

    except ValueError:
        print("Error: Please enter valid numeric scores!")
        return None

    total = (
        sum(Compulsories.values()) +
        sum(Sciences.values()) +
        sum(Technicals.values()) +
        sum(Humanities.values())
    )

    mean_score = round(total / 12)  # ✅ Fixed divisor
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
while True:
    try:
        confirmation = int(input(
        "Hello! Welcome to the student management system.\n"
        "(1: Add a new student, 2: Calculate student grade): "
    ))
        if confirmation in [1, 2]:
            break  # valid input → exit loop

        else:
            print("Error: Please enter either 1 or 2.")

    except ValueError:
        print("Error: Please enter a valid number!")


# -------- ADD STUDENT --------
if confirmation == 1:
    Name = input("Enter the name of the new student: ").strip().title()

    try:
        Admission_number = int(input("Enter the admission number: "))
    except ValueError:
        print("Error: Admission number must be a number!")
        exit()

    Class = input("Enter the class: ").lower().replace(" ", "")

    if Class in students_dictionary:

        if Name in students_dictionary[Class]:
            print("Error: Student already exists in this class!")

        else:
            students_dictionary[Class][Name] = {
                "Admission_number": Admission_number,
                "Grade": None
            }
            print(f"Student {Name} added successfully to {Class}.")

    else:
        print("Error: Invalid class!")


# -------- CALCULATE GRADE --------
elif confirmation == 2:

    # -------- GET VALID CLASS --------
    while True:
        student_class = input("Enter your class: ").lower().replace(" ", "")

        if student_class in students_dictionary:
            break
        else:
            print("Error: Invalid class! Choose between form1, form2, form3, or form4.")

    # -------- GET VALID ADMISSION NUMBER --------
    while True:
        try:
            number = int(input("Enter your admission number: "))
        except ValueError:
            print("Error: Admission number must be a number!")
            continue

        # Check if admission number exists in that class
        found = False
        for name, details in students_dictionary[student_class].items():
            if details["Admission_number"] == number:
                found = True
                break

        if found:
            break
        else:
            print("Error: Admission number not found in this class. Try again.")

    # -------- PROCESS STUDENT --------
    for name, details in students_dictionary[student_class].items():
        if details["Admission_number"] == number:

            grade = calculate_mean_score()

            if grade is None:
                break

            students_dictionary[student_class][name]["Grade"] = grade

            print(f"\nHello, {name}!")

            if grade == "A":
                print("Excellent! Keep this up")
            elif grade == "A-":
                print("Great job! You're doing so nicely")
            elif grade == "B+":
                print("You're getting there")
            elif grade == "B":
                print("Wonderful! But dont give up yet")
            elif grade == "B-":
                print("Great Job but improve this grade")
            elif grade == "C+":
                print("You're passing but you're not there yet")
            elif grade == "C":
                print("You can do better")
            elif grade == "C-":
                print("You need to work harder")
            elif grade == "D+":
                print("Please pull up your socks, you're at risk of failing")
            elif grade == "D":
                print("You are at a terrible risk of failing, you need to improve")
            else:
                print("You failed")

            print("\nClass Logbook:")
            print(students_dictionary[student_class][name])


# -------- INVALID OPTION --------
else:
    print("Error: Invalid option selected!")

# Things to do
# 1. Add option to update student details
# 2. Add option to delete student
# 3. Add option to view all students in a class
# 4. Add option to view all students in the school
# 5. Have a method to store all students into in a separate file (e.g. CSV, JSON) for persistence
# 6. Add option to load students from a file when the program starts
