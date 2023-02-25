class Semester:
    def __init__(self, semester_name):
        self.semester_name = semester_name
        self.courses = []

    def add_course(self, course):
        # Add a course to the semester's list of courses
        self.courses.append(course)

    def remove_course(self, course):
        # Remove a course from the semester's list of courses
        self.courses.remove(course)

    def get_courses(self):
        # Return a list of the courses for the semester
        return self.courses

class Course:
    def __init__(self, course_code, course_name, credit_hours):
        self.course_code = course_code
        self.course_name = course_name
        self.credit_hours = credit_hours
        self.semesters = []

    def add_semester(self, semester):
        # Add a semester to the course's list of semesters
        self.semesters.append(semester)
        semester.add_course(self)

    def remove_semester(self, semester):
        # Remove a semester from the course's list of semesters
        self.semesters.remove(semester)
        semester.remove_course(self)

    def get_semesters(self):
        # Return a list of the semesters for the course
        return self.semesters
