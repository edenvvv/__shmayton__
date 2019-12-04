class Question:
    def __init__(self, course_name='', difficulty=0, solution_kind=None, semester='A',  year=0, exam_date='A',
                 question_format='Image', subtopic=''):
        self.course_name = course_name
        self.difficulty = difficulty
        self.solution_kind = solution_kind
        self.semester = semester
        self.year = year
        self.exam_date = exam_date
        self.question_format = question_format
        self.subtopic = subtopic

    def get_course_name(self):
        return self.course_name

    def set_course_name(self, name):
        self.course_name = name

    def get_difficulty(self):
        return self.difficulty

    def set_difficulty(self, diff):
        self.difficulty = diff

    def get_solution_kind(self):
        return self.solution_kind

    def set_solution_kind(self, solution_type):
        self.solution_kind = solution_type

    def get_semester(self):
        return self.semester

    def set_semester(self, question_semester):
        self.semester = question_semester

    def get_year(self):
        return self.year

    def set_year(self, question_year):
        self.year = question_year

    def get_exam_date(self):
        return self.exam_date

    def set_exam_date(self, question_exam_date):
        self.exam_date = question_exam_date

    def get_question_format(self):
        return self.question_format

    def set_question_format(self, question__format):
        self.question_format = question__format

    def get_subtopic(self):
        return self.subtopic

    def set_subtopic(self, question_subtopic):
        self.subtopic = question_subtopic


class Professor:
    def __init__(self, name='', phone_number='', topic='', password=''):
        self.name = name
        self.phone_number = phone_number
        self.topic = topic
        self.password = password

    def get_name(self):
        return self.name

    def set_name(self, professor_name):
        self.name = professor_name

    def get_phone(self):
        return self.phone_number

    def set_phone(self, professor_phone):
        self.phone_number = professor_phone

    def get_topic(self):
        return self.topic

    def set_topic(self, professor_topic):
        self.topic = professor_topic

    def get_password(self):
        return self.password

    def set_password(self, professor_password):
        self.password = professor_password


class Student:
    def __init__(self, name=''):
        self.name = name

    def get_name(self):
        return self.name

    def set_name(self, student_name):
        self.name = student_name


class Coordinator:
    def __init__(self, coordinator_name='', phone_number='', password=''):
        self.coordinator_name = coordinator_name
        self.phone_number = phone_number
        self.password = password

    def get_coordinator_name(self):
        return self.coordinator_name

    def set_coordinator_name(self, name):
        self.coordinator_name = name

    def get_phone_number(self):
        return self.phone_number

    def set_phone_number(self, coordinator_phone_number):
        self.phone_number = coordinator_phone_number

    def get_password(self):
        return self.password

    def set_password(self, coordinator_password):
        self.password = coordinator_password


"""class Test:
    def __init__(self, course_name='', semester='A', year=0, exam_date='A'):
        self.course_name = course_name
        self.semester = semester
        self.year = year
        self.exam_date = exam_date

    def get_course_name(self):
        return self.course_name

    def get_semester(self):
        return self.semester

    def get_year(self):
        return self.year

    def exam_date(self):
        return self.exam_date"""