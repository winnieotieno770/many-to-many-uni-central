import datetime
class Student():
    all = []
    def __init__(self,name,):
        self.name = name
        Student.all.append(self) 

    def all_student_enrollments(self):
        return [e for e in Enrollment.all if e.student == self ]
    
    def __repr__(self):
       return f"Student name : {self.name}"

class Course():
    all = []
    def __init__(self,title):
        self.title = title
        Course.all.append(self)

    def all_course_enrollements(self):
        return [enrollement for enrollement in Enrollment.all if enrollement.course == self]
    
    def __repr__(self):
       return f"Student course : {self.title}"

class Enrollment():
    all = []
    def __init__(self, student, course):
        self.student = student
        self.course = course
        self.date = datetime.datetime.now()
        Enrollment.all.append(self)
    def __repr__(self):
        return f"              Enrollment Details    \n Student name: {self.student.name} \n Student course: {self.course.title}"



