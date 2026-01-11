import datetime

class Student():
    all = []
    def __init__(self, name):
        self.name = name
        Student.all.append(self) 

    def all_student_enrollments(self):
        # Returns all enrollment objects linked to this student
        return [e for e in Enrollment.all if e.student == self]
    
    def __repr__(self):
       return f"Student name : {self.name}"

class Course():
    all = []
    def __init__(self, title):
        self.title = title
        Course.all.append(self)

    def all_course_enrollements(self):
        # Returns all enrollment objects linked to this course
        return [e for e in Enrollment.all if e.course == self]
    
    def __repr__(self):
      return f"Course title: {self.title}"

class Enrollment():
    all = []
    def __init__(self, student, course):
        self.student = student
        self.course = course
        
        self.date = datetime.datetime.now()
        Enrollment.all.append(self)

    def __repr__(self):
        return (f"              Enrollment Details    \n"
                f" Student name: {self.student.name} \n"
                f" Student course: {self.course.title} \n"
                f" Date: {self.date.strftime('%Y-%m-%d %H:%M:%S')}")


if __name__ == "__main__":
    print("Universal student universe")
    
    student1 = Student("Jamie")
    course1 = Course("Computer Science")
    enrollment1 = Enrollment(student1, course1)

    print(enrollment1)
