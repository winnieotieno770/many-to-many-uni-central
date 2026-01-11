import datetime

class Student:
    all = []
    def __init__(self, name):
        self.name = name
        Student.all.append(self) 

    def all_student_enrollments(self):
        return [e for e in Enrollment.all if e.student == self]

    def enroll_in_course(self, course): # Standardized name
        # Prevent duplicates
        if course not in self.all_student_courses():
            Enrollment(self, course)
    
    def all_student_courses(self):
        return [e.course for e in self.all_student_enrollments()]
    
    def __repr__(self):
       return f"<Student: {self.name}>"

class Course:
    all = []
    def __init__(self, title):
        self.title = title
        Course.all.append(self)

    def enroll_student(self, student):
        if student not in self.all_course_students():
            Enrollment(student, self)

    def all_course_enrollments(self): # Fixed spelling
        return [e for e in Enrollment.all if e.course == self]
    
    def all_course_students(self): 
        return [e.student for e in self.all_course_enrollments()]
    
    def __repr__(self):
      return f"<Course: {self.title}>"

class Enrollment:
    all = []
    def __init__(self, student, course):
        self.student = student
        self.course = course        
        self.date = datetime.datetime.now()
        Enrollment.all.append(self)

    def __repr__(self):
        return (f"--- Enrollment Details ---\n"
                f"Student: {self.student.name}\n"
                f"Course: {self.course.title}\n"
                f"Date: {self.date.strftime('%Y-%m-%d %H:%M:%S')}")
if __name__ == "__main__":
    s1 = Student("Jamie")
    c1 = Course("Computer Science")
    
    # Simple, direct instantiation
    Enrollment(s1, c1)

    # Testing the many-to-many lookup
    print(f"{s1.name}'s courses: {s1.all_student_enrollments()}")
    print(f"{c1.title} students: {c1.all_course_students()}")
