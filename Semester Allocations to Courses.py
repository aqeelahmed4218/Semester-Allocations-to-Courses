from abc import ABC, abstractmethod

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

class BaseCourse(ABC):
    def __init__(self, course_code, course_name, credit_hours):
        self.course_code = course_code
        self.course_name = course_name
        self.credit_hours = credit_hours

    @abstractmethod
    def get_info(self):
        pass

class MajorCourse(BaseCourse):
    def __init__(self, course_code, course_name, credit_hours, required_courses):
        super().__init__(course_code, course_name, credit_hours)
        self.required_courses = required_courses

    def get_info(self):
        return f"{self.course_code} - {self.course_name}, {self.credit_hours} credits, required courses: {', '.join(self.required_courses)}"

class ElectiveCourse(BaseCourse):
    def __init__(self, course_code, course_name, credit_hours, elective_group):
        super().__init__(course_code, course_name, credit_hours)
        self.elective_group = elective_group

    def get_info(self):
        return f"{self.course_code} - {self.course_name}, {self.credit_hours} credits, elective group: {self.elective_group}"

class Course:
    def __init__(self, base_course, semesters):
        self.base_course = base_course
        self.semesters = semesters

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

    def get_info(self):
        return self.base_course.get_info()
