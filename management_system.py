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
