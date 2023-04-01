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

# Example usage:

# Create courses
cs101 = BaseCourse("CS101", "Introduction to Computer Science", 3)
cs201 = BaseCourse("CS201", "Data Structures and Algorithms", 4)
cs301 = MajorCourse("CS301", "Advanced Algorithms", 3, ["CS201", "CS202"])
cs350 = ElectiveCourse("CS350", "Topics in Computer Science", 3, "Artificial Intelligence")

# Create semesters
fall2023 = Semester("Fall 2023")
spring2024 = Semester("Spring 2024")

# Create course instances
course1 = Course(cs101, [fall2023])
course2 = Course(cs201, [spring2024])
course3 = Course(cs301, [spring2024])
course4 = Course(cs350, [fall2023, spring2024])

# Add courses to semesters
fall2023.add_course(course1)
fall2023.add_course(course4)
spring2024.add_course(course2)
spring2024.add_course(course3)
spring2024.add_course(course4)

# Print course info
print(course1.get_info())
print(course2.get_info())
print(course3
