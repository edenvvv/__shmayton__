from docx import Document
import os


def create_word_file(name, path_list):
    document = Document()
    for path in path_list:
        document.add_picture(path)
    document.save(f'{name}.docx')
    return os.startfile(f'{name}.docx')


"""
Examples: create_word_file('test', ['C:/Users/Top/Desktop/shmython/GUI/questions/gigi.PNG',
                        'C:/Users/Top/Desktop/shmython/GUI/questions/gogo.PNG'])
"""