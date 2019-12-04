import sqlite3


conn = sqlite3.connect('data.db')
# Creates connection to database

curs = conn.cursor()


# Creates cursor to database


"""
Functions for receiving and storing information
"""


def convert_to_binary_data(photo):
    """Convert digital data to binary format"""
    with open(photo, 'rb') as file:
        blob_data = file.read()
    return blob_data


def write_to_file(data, photo):
    """Convert binary data to proper format and write it on Hard Disk"""
    with open(photo, 'wb') as file:
        file.write(data)


def create_table():
    # create table for the data we get from the user
    with conn:
        curs.execute("""CREATE TABLE IF NOT EXISTS user_data (
            question_photo BLOB PRIMARY KEY,
            course_name TEXT NOT NULL,
            question_name TEXT NOT NULL,
            difficult_level TEXT,
            source TEXT,
            semester TEXT,
            deadline TEXT,
            question_format TEXT,
            solution TEXT,
            solution_type TEXT,
            year TEXT
        ) """)


def insert_data(test):
    with conn:
        photo = convert_to_binary_data(test.question_photo)
        # Convert data into tuple format
        curs.execute("INSERT INTO user_data VALUES (?,?,?,?,?,?,?,?,?,?,?)", (photo, test.course_name,
                                                                              test.question_name, test.difficult_level,
                                                                              test.source, test.semester, test.deadline,
                                                                              test.question_format, test.solution,
                                                                              test.solution_type, test.year))


def get_test_info(course_name, name, level, year):
    if level and year is not '':
        curs.execute("SELECT * FROM user_data WHERE course_name = :course_name AND question_name=:question_name"
                     " AND difficult_level=:level AND year=:year",
                     {'course_name': course_name, 'question_name': name, 'level': level, 'year': year})
    elif year is not '':
        curs.execute("SELECT * FROM user_data WHERE course_name = :course_name AND question_name=:question_name"
                     " AND year=:year", {'course_name': course_name, 'question_name': name, 'year': year})
    elif level is not '':
        curs.execute("SELECT * FROM user_data WHERE course_name = :course_name AND question_name=:question_name"
                     " AND difficult_level=:level", {'course_name': course_name, 'question_name': name, 'level': level})
    else:
        curs.execute("SELECT * FROM user_data WHERE course_name = :course_name AND question_name=:question_name",
                     {'course_name': course_name, 'question_name': name})
    return curs.fetchall()


def update_difficult_level(test, difficult_level):
    with conn:
        curs.execute("""UPDATE user_data SET difficult_level = :difficult_level
                    WHERE course_name = :course_name AND question_name=:question_name""",
                     {'course_name': test['course_name'], 'question_name': test['question_name'],
                      'difficult_level': difficult_level})


def remove_question(test):
    with conn:
        curs.execute("DELETE from user_data WHERE course_name = :course_name AND question_name=:question_name",
                     {'course_name': test['course_name'], 'question_name': test['question_name']})


def commit_db():
    conn.commit()


def close_db():
    conn.close()
