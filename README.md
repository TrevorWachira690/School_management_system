# Student Grading & School Management System

A Python-based school management system designed to handle student records, grading, and academic performance tracking across multiple classes.

This project simulates a real-world school database and provides functionality for managing student information, assigning grades, and organizing academic data in a structured and scalable way.

---

## Overview

The **Student Grading & School Management System** simplifies how schools manage student data. It organizes students into different forms (classes), assigns admission numbers, and tracks academic performance.

The system is designed with scalability in mind, making it easy to extend into a full-featured school management platform.

---

## Features

- Organized student database by class (Form 1, Form 2, etc.)
-  Unique admission number assignment for each student
-  Grade recording and updates
-  Student lookup functionality
-  Input validation for error handling (e.g., invalid student names)
-  Modular and expandable structure for future development

---

## Technologies Used

- Python 3
- Core Python concepts:
  - Dictionaries (for database structure)
  - Functions
  - Conditional statements
  - User input handling

---

## Project Structure

```bash
student-grading-system/
│
├── main.py              # Main application logic
├── database.py          # Student data structure (optional separation)
├── utils.py             # Helper functions (optional)
└── README.md            # Project documentation
```

---

## How It Works

The system uses a nested dictionary to store student data:

```python
students_dictionary = {
    "form1": {
        "John": {"Admission_number": 5800, "Grade": None},
        "Mary": {"Admission_number": 5801, "Grade": None}
    }
}
```

### Core Flow:

1. User inputs student name  
2. System checks if student exists  
3. If valid:  
   - Displays or updates student grade  
4. If invalid:  
   - Displays error and exits program  

---

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/student-grading-system.git
cd student-grading-system
```

### 2. Run the program

```bash
python main.py
```

---

## Current Limitations

- Data is stored in-memory (not persistent)
- No graphical user interface (CLI only)
- Limited to basic grading functionality
- Manual input required for all operations
- Lacks a method of individual data storage of student records
---

## Ongoing Improvements

- Improved error handling and validation  
- Cleaner modular code structure  
- Separation of logic into functions and files  
- Refactoring database structure for scalability  
- Enhancing user interaction flow  

---

## Future Improvements

### Database Integration
- Integration with SQLite / MySQL / PostgreSQL  
- Persistent student records  

### User Interface
- GUI using Tkinter / PyQt  
- Web-based interface using Flask or Django  

### Advanced Features
- Teacher and admin roles  
- Subject-based grading system  
- Report card generation  
- GPA and performance analytics  

### Online Capabilities
- Student login portals  
- Cloud-based access  
- API integration  

### Security Enhancements
- Authentication system  
- Role-based access control  

---

## Vision

The long-term goal is to evolve this project into a fully functional school ERP system capable of handling:

- Student management  
- Academic tracking  
- Staff management  
- Communication systems  

---

## Contributing

Contributions are welcome!

1. Fork the repository  
2. Create a new branch  
3. Make your changes  
4. Submit a pull request  

---

## License

This project is open-source and available under the MIT License.

---

## Author

- Trevor Mbiriri  
- Aspiring Software Engineer | Python Developer 
- [Github profile](https://github.com/TrevorWachira690)
