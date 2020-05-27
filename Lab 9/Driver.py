import sys
from University import Uni

def main():
    c = Uni()
    print("---------------------------------------------------------------------------")
    print("All the Courses: \n")
    c.add_courses(1, "English 1000", 3, "English")
    c.add_courses(2, "Math 1000", 3, "Math")
    c.add_courses(3, "Biology 1000", 3, "Science")
    c.add_courses(4, "Music 1000", 3, "Music")
    c.show_courses()
    print("---------------------------------------------------------------------------")
    print("Find Courses using ID: \n")
    c.find_idcourse(2)
    print("---------------------------------------------------------------------------")
    c.add_student(1, "Roi Chico")
    c.add_student(2, "Billy Bob")
    print("Find Students using ID: \n")
    c.find_idstudent(2)
    print("---------------------------------------------------------------------------")
    print("\nStudents Classes:")
    c.class_enrollments(1, 1)
    c.class_enrollments(1, 2)
    c.class_enrollments(2, 3)
    c.class_enrollments(2, 4)
    c.show_enrollments()
    print("---------------------------------------------------------------------------")
    print("\nStudents Classes after dropping classes:")
    c.drop_course(2, 4)
    c.show_enrollments()
    print("---------------------------------------------------------------------------")
    print("\nStudents Classes after a student gets expelled:")
 #   c.drop_student("Roi Chico")
 #   c.show_enrollments()


if __name__ == "__main__":
    sys.exit(main())

