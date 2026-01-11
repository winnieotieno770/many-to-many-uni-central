markdown
# 🎓 StudentUniverse: Many-to-Many Enrollment System

**StudentUniverse** is a Python-based implementation of a complex Many-to-Many (N:M) relationship between Students and Courses. Built with **Object-Oriented Programming (OOP)** principles, it utilizes a **Join Class (Associative Entity)** architecture to manage bidirectional data and metadata tracking.

## 🌟 Key Features
*   **Join Class Architecture**: Uses an `Enrollment` class to "bridge" students and courses, allowing the system to store relationship-specific data (like enrollment timestamps).
*   **Data Integrity**: Features built-in guard clauses to prevent duplicate enrollments for the same student-course pair.
*   **Bidirectional Lookups**: Query a student’s full course history or a course’s student roster with optimized list comprehensions.
*   **Clean Debugging**: Implements custom `__repr__` methods for professional, human-readable console output.

## 🚀 Quick Start

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/winnieotieno770/many-to-many-uni-central.git
   cd mamy-to-many-uni-central
Use code with caution.

Run the script:
bash
python enrollment_system.py
Use code with caution.

Usage Example
python
from enrollment_system import Student, Course

# 1. Initialize data entities
s1 = Student("Jamie")
c1 = Course("Computer Science 101")

# 2. Establish relationship via the Enrollment system
s1.enroll_in_course(c1)

# 3. Query the many-to-many relationship
print(s1.all_student_courses())    # Returns: [<Course: Computer Science 101>]
print(c1.all_course_students())   # Returns: [<Student: Jamie>]

# 4. Attempt a duplicate (Handled by Guard Clause)
s1.enroll_in_course(c1)           # Output: "Notice: Jamie is already enrolled..."