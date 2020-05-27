class Student:
    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name

    def __str__(self):
        return str(self.student_id) + ' ' + self.student_name

    def getStudent(self):
        return [self.student_id, self.student_name]