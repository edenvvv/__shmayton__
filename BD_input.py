import DB as sql
from data import Data
from pdf import pdf_split
import classes


def input_message(message):
    temp = input(message)
    if temp == '':
        temp = None
    return temp


switch = {
    'insert': sql.insert_data,
    'update': sql.update_difficult_level,
    'remove': sql.remove_question,
    'pdf': pdf_split
}

sql.create_table()

while True:
    decision = input("""
What you want to do?
Write 'insert' to insert question
Write 'update' to update difficult level
Write 'remove' to remove question
Write 'pdf' to create a word file
""")

    if decision.lower() == 'insert':
        try:
            question_photo = input('enter the path of question photo (Examples: C:/Users/Top/Desktop/name.PNG)  ')
            course_name = input('enter the course name  ')
            question_name = input('enter the question name  ')
            if question_photo == '' or course_name == '' or question_name == '':
                raise NameError
            difficult_level = input_message('enter the difficult level (Optional)  ')
            source = input_message('enter the source (Optional)  ')
            semester = input_message('enter the semester (Optional)  ')
            deadline = input_message('enter the deadline (Optional)  ')
            question_format = input_message('enter the question format (Optional)  ')
            solution = input_message('enter the solution (Optional)  ')
            solution_type = input_message('enter the solution type (Optional)  ')
            year = input_message('enter the year (Optional)  ')

            question = classes.Question(course_name, difficult_level, solution_type, semester, year, deadline,
                                        question_format)

            test = Data(question_photo, question, question_name, source, solution)
            switch[decision](test)
            print('The process was successful')
            booli = input('Do you want to continue? (for no press enter) ')
            if booli:
                break
        except NameError:
            print("The fields 'question photo','course name' and 'question name' are a must, Try again")
        except Exception:
            print("Something went wrong, Try again")

    elif decision.lower() == 'update':
        try:
            course_name = input('enter the course name of the question you want to change  ')
            question_name = input('enter the question name of the question you want to change  ')
            new_difficult_level = input('enter the new difficult level  ')
            if new_difficult_level == '' or course_name == '' or question_name == '':
                raise NameError
            test = {'course_name': course_name,
                    'question_name': question_name
                    }
            switch[decision](test, new_difficult_level)
            print('The process was successful')
            booli = input('Do you want to continue? (for no press enter) ')
            if booli:
                break
        except NameError:
            print("The fields 'new difficult level','course name' and 'question name' are a must, Try again")
        except Exception:
            print("Something went wrong, Try again")

    elif decision.lower() == 'remove':
        try:
            course_name = input('enter the course name of the question you want to remove  ')
            question_name = input('enter the question name of the question you want to remove  ')
            if course_name == '' or question_name == '':
                raise NameError
            test = {'course_name': course_name,
                    'question_name': question_name
                    }
            switch[decision](test)
            print('The process was successful')
            booli = input('Do you want to continue? (for no press enter) ')
            if booli:
                break
        except NameError:
            print("The fields 'course name' and 'question name' are a must, Try again")
        except Exception:
            print("Something went wrong, Try again")

    elif decision.lower() == 'pdf':
        try:
            path = input('enter the path to the pdf  ')
            pdf_split(path)
        except Exception:
            print("Something went wrong, Try again")






# Examples: test1 = Data('C:/Users/Top/Desktop/shmython/GUI/questions/gigi.PNG', 'math', 'Invoice set', '5')
