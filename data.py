class Data:

    def __init__(self, question_photo, question_data, question_name, source, solution=None):
        self.question_photo = question_photo
        self.course_name = question_data.get_course_name()
        self.question_name = question_name
        self.difficult_level = question_data.get_difficulty()
        self.source = source  # from a test or examiner ?
        self.semester = question_data.get_semester()
        self.deadline = question_data.get_exam_date()  # test deadline a or b ?
        self.question_format = question_data.get_question_format()  # PDF/JPG ?
        self.solution = solution  # there is a solution ?
        self.solution_type = question_data.get_solution_kind()
        self.year = question_data.get_year()

    def __repr__(self):
        return f"""test data is ('{self.question_photo}', '{self.course_name}', '{self.question_name}', 
                '{self.difficult_level}','{self.source}', '{self.semester}', '{self.deadline}',
                '{self.question_format}', '{self.solution}','{self.solution_type}', '{self.year}')"""

    def get_question_name(self):
        return self.question_name

    def get_question_photo(self):
        return self.question_photo

    def get_course_name(self):
        return self.course_name

    def get_difficult_level(self):
        return self.difficult_level

    def get_year(self):
        return self.year

    def get_source(self):
        return self.source

    def get_semester(self):
        return self.semester

    def get_deadline(self):
        return self.deadline

    def get_question_format(self):
        return self.question_format

    def get_solution(self):
        return self.solution

    def get_solution_type(self):
        return self.solution_type
