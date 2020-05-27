class Course:
    def __init__(self, course_id, course_name, credits, department):
        self.course_id = course_id
        self.course_name = course_name
        self.credits = credits
        self.department = department

    def __str__(self):
        return 'Course ID: ' + str(self.course_id) + '\nCourse Name: ' + self.course_name + '\nCourse Credits: ' + str(self.credits) + '\nCourse Department: ' + self.department + '\n'

    def getCourse(self):
        return [self.course_id, self.course_name, self.credits, self.department]
