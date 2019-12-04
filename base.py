import tkinter as tk
import DB as sql
from create_docx import create_word_file
import os

HEIGHT = 600
WIDTH = 1000

sql.create_table()


def create_folder(name, level, year):
    new_path = f'C:/Users/Top/Desktop/shmython/GUI/{name}/{level}/{year}'
    if not os.path.exists(new_path):
        os.makedirs(new_path)


def open_folder(name, level, year):
    path = f'C:/Users/Top/Desktop/shmython/GUI/{name}/{level}/{year}'
    path = os.path.realpath(path)
    os.startfile(path)


def create_word(course_name, question_name, difficult_level, year):
    try:

        if course_name == '' or question_name == '':
            # Checks if the received name course and question name is not empty
            raise NameError

        all_data = sql.get_test_info(course_name, question_name, difficult_level, year)

        empty_list = []

        if all_data == empty_list:
            # Checks if the received name course and question name are the same as the database
            raise ValueError

        create_folder(question_name, difficult_level, year)

        count = 1

        word_list = []
        for row in all_data:
            photo_data = row[0]
            # Saves the image information
            photo_path = f'C:/Users/Top/Desktop/shmython/GUI/{question_name}/{difficult_level}/{year}/{count}.jpg'
            # Creates the location where the image will be saved
            sql.write_to_file(photo_data, photo_path)
            word_list.append(photo_path)
            label.insert(tk.END, f"{count}) {row[1:]} ")
            # print in label
            count += 1

        create_word_file(question_name, word_list)


    except NameError:
        mess = "Must enter course name and question name"
        gui_print(mess)
    except ValueError:
        mess = "The names do not exist in the database"
        gui_print(mess)
    except Exception:
        mess = "Something went wrong"
        gui_print(mess)


def search_question(course_name, question_name, difficult_level, year):
    try:

        if course_name == '' or question_name == '':
            # Checks if the received name course and question name is not empty
            raise NameError

        all_data = sql.get_test_info(course_name, question_name, difficult_level, year)

        empty_list = []

        if all_data == empty_list:
            # Checks if the received name course and question name are the same as the database
            raise ValueError

        create_folder(question_name, difficult_level, year)

        count = 1

        for row in all_data:
            photo_data = row[0]
            # Saves the image information
            photo_path = f'C:/Users/Top/Desktop/shmython/GUI/{question_name}/{difficult_level}/{year}/{count}.jpg'
            # Creates the location where the image will be saved
            sql.write_to_file(photo_data, photo_path)
            label.insert(tk.END, f"{count}) {row[1:]} ")
            # print in label
            count += 1

        open_folder(question_name, difficult_level, year)
    except NameError:
        mess = "Must enter course name and question name"
        gui_print(mess)
    except ValueError:
        mess = "The names do not exist in the database"
        gui_print(mess)
    except Exception:
        mess = "Something went wrong"
        gui_print(mess)


def gui_print(message):
    label.insert(tk.END, f"{message}, Try again")
    # print in label


root = tk.Tk()
# Creates the program window


canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
# Creates the window in "canvas" size
canvas.pack()
# Shows the window in "canvas" size


background_image = tk.PhotoImage(file='landscape.png')
# Takes a photo as input
background_label = tk.Label(root, image=background_image)
# Uses image as background
background_label.place(relwidth=1, relheight=1)
# Shows it in The specified coordinates


frame1 = tk.Frame(root, bg='#80c1ff', bd=5)
# Creates the frame Light blue (#80c1ff)
frame1.place(relx=0.2, rely=0.05, relwidth=0.3, relheight=0.15, anchor='n')
# Shows the frame in The specified coordinates

entry1 = tk.Entry(frame1, font=40)
# Creates a input box
entry1.place(rely=0.2, relwidth=1, relheight=0.8)
# Shows the input box

label1 = tk.Label(frame1, text='course name:', bg='#80c1ff', font=('courier', 10), anchor='nw', bd=4)
# Creates a label
label1.place(relx=0.12, rely=0, relwidth=0.35, relheight=0.3)
# Shows the label


frame2 = tk.Frame(root, bg='#80c1ff', bd=5)
# Creates the frame Light blue (#80c1ff)
frame2.place(relx=0.45, rely=0.05, relwidth=0.2, relheight=0.15, anchor='n')
# Shows the frame in The specified coordinates

entry2 = tk.Entry(frame2, font=40)
# Creates a input box
entry2.place(rely=0.2, relwidth=1, relheight=0.8)
# Shows the input box

label2 = tk.Label(frame2, text='question name:', bg='#80c1ff', font=('courier', 10), anchor='nw', bd=4)
# Creates a label
label2.place(relx=0.12, rely=0, relwidth=0.63, relheight=0.3)
# Shows the label


frame3 = tk.Frame(root, bg='#80c1ff', bd=5)
# Creates the frame Light blue (#80c1ff)
frame3.place(relx=0.65, rely=0.05, relwidth=0.2, relheight=0.15, anchor='n')
# Shows the frame in The specified coordinates

entry3 = tk.Entry(frame3, font=40)
# Creates a input box
entry3.place(rely=0.2, relwidth=1, relheight=0.8)
# Shows the input box

label3 = tk.Label(frame3, text='difficulty level:', bg='#80c1ff', font=('courier', 10), anchor='nw', bd=4)
# Creates a label
label3.place(relx=0.12, rely=0, relwidth=0.75, relheight=0.3)
# Shows the label


frame4 = tk.Frame(root, bg='#80c1ff', bd=5)
# Creates the frame Light blue (#80c1ff)
frame4.place(relx=0.85, rely=0.05, relwidth=0.2, relheight=0.15, anchor='n')
# Shows the frame in The specified coordinates

entry4 = tk.Entry(frame4, font=40)
# Creates a input box
entry4.place(rely=0.2, relwidth=0.5, relheight=0.8)
# Shows the input box

label4 = tk.Label(frame4, text='year:', bg='#80c1ff', font=('courier', 10), anchor='nw', bd=4)
# Creates a label
label4.place(relx=0.12, rely=0, relwidth=0.25, relheight=0.3)
# Shows the label


button = tk.Button(frame4, text="Search", font=40,
                   command=lambda: search_question(entry1.get(), entry2.get(), entry3.get(), entry4.get()))
# entry1.get() = course_name, entry2.get() = question name, entry3.get() = difficult_level, entry4.get() = year
# Creates a button
button.place(relx=0.55, rely=0.2, relwidth=0.45, relheight=0.8)
# Shows the button


lower_frame = tk.Frame(root, bg='#80c1ff', bd=10)
# Creates the lower frame Light blue (#80c1ff)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')
# Shows the lower frame in The specified coordinates

scrollbar = tk.Scrollbar(lower_frame)
# Creates a scrollbar
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
# Shows the scrollbar
label = tk.Listbox(lower_frame, font=('courier', 12), yscrollcommand=scrollbar.set)
# Creates a label
label.place(relwidth=0.9761, relheight=1)
# Shows the label
scrollbar.config(command=label.yview)


word_button = tk.Button(root, text="create word file", font=40,
                        command=lambda: create_word(entry1.get(), entry2.get(), entry3.get(), entry4.get()))
# entry1.get() = course_name, entry2.get() = question name, entry3.get() = difficult_level, entry4.get() = year
# Creates a button
word_button.place(relx=0.37, rely=0.87, relwidth=0.25, relheight=0.1)
# Shows the button

root.mainloop()
# Run the program window


sql.close_db()