from Courses import Course
from Student import Student

class Uni:
    def __init__(self):
        self.students = []
        self.courses = []
        self.enroll = {}

    def add_courses(self, course_id, course_name, credits, department):
        self.courses.append(Course(course_id, course_name, credits, department))

    def show_courses(self):
        if(len(self.courses) > 0):
            for index in range(0,len(self.courses)):
                print(self.courses[index])

    def find_idcourse(self, id):
        if(len(self.courses) > 0):
            for index in range(0,len(self.courses)):
                [course_id, course_name, credits, department] = self.courses[index].getCourse()
                if(id == course_id):
                    print(self.courses[index])

    def find_course(self, id):
        if(len(self.courses) > 0):
            for index in range(0,len(self.courses)):
                [course_id, course_name, credits, department] = self.courses[index].getCourse()
                if(id == course_id):
                    return self.courses[index]
            return -1
        else:
            return -1
    
    def add_student(self, student_id, student_name):
        self.students.append(Student(student_id, student_name))

#    def drop_student(self, name):
#       if(len(self.students) > 0):
#            for index in range(0,len(self.students)):
#                [student_id, student_name] = self.students[index].getStudent()
#                if(name == student_name):
#                    print(self.students[index].remove(Student))

    def find_idstudent(self, id):
        if(len(self.students) > 0):
            for index in range(0,len(self.students)):
                [student_id, student_name] = self.students[index].getStudent()
                if(id == student_id):
                    print(self.students[index])

    def find_student(self, id):
        if(len(self.students) > 0):
            for index in range(0,len(self.students)):
                [student_id, student_name] = self.students[index].getStudent()
                if(id == student_id):
                    return self.students[index]
            return -1
        else:
            return -1

    def class_enrollments(self, student_id, course_id):
        student = self.find_student(student_id)
        course = self.find_course(course_id)
        if(student == -1 or course == -1):
            print("Student or course doesn't exist")
        else:
            courseList = self.enroll.get(student, -1)
            if(courseList == -1):
                self.enroll[student] = [course]
            else:
                self.enroll[student].append(course)

    def show_enrollments(self):
        enrolled = self.enroll.keys()
        enrolledList = list(enrolled)
        if(len(enrolled) > 0):
            for index in range(0,len(enrolled)):
                print(enrolledList[index] , " is enrolled in :")
                classes = self.enroll[enrolledList[index]]
                for sec in range(0,len(classes)):
                    print(classes[sec])
        else:
            print("No students enrolled")

    def drop_course(self, student_id, course_id):
        student = self.find_student(student_id)
        course = self.find_course(course_id)
        if(student == -1 or course == -1):
            print("Student or course doesn't exist")
        else:
            courseList = self.enroll.get(student, -1)
            if(courseList == -1):
                self.enroll[student] = [course]
            else:
                self.enroll[student].remove(course)

