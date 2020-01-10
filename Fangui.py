import tkinter
from tkinter import messagebox
import user_db as db
import base as main
import DB_input as input_ui
db.create_table()
top = tkinter.Tk()
# open a page
user_name = tkinter.StringVar
email = tkinter.StringVar
password = tkinter.StringVar
# saves personal accounts for transfer
cor = tkinter.IntVar()
prof = tkinter.IntVar()
stu = tkinter.IntVar()


def input_database(str3, stop):
    """input the data into the database"""
    data_type = db.get_data(str3)
    if data_type[0] != "student":
        stop.destroy()
        input_ui.input_data()
    else:
        messagebox.showinfo("No access", "Access denied")


def complete_register(str1, str2, int1, int2, int3):
    """Confirms user status and logs in to the database"""
    messagebox.showinfo("complete registration", "the registration is completed")

    """
    if int1 == 0 or int2 == 0 or int3 == 0:
        str3 = "Must select status"
    """

    if int1 == 1:
        str3 = "coordinator"
    if int2 == 1:
        str3 = "professor"
    if int3 == 1:
        str3 = "student"

    """
    if int1 == 1 and int2 == 1 or int1 == 1 and int3 == 1 or int2 == 1 and int3 == 1:
        str3 = "You cannot select more than one status"
    """

    db.insert_data(str3, str1, str2)

# message after clicking a button


def login(str1, str2):
    """Validation of login interface"""
    data = db.get_data(str1)
    if data[1] == str1 and data[2] == str2:
        main.main()
    else:
        messagebox.showinfo("Login faild", "wrong username/password")


def openapage2():
    """Responsible for login interface"""
    root2 = tkinter.Toplevel()
    # creating another page "layer"
    top.withdraw()
    p = tkinter.Canvas(root2, height=400, width=500)
    background_image2 = tkinter.PhotoImage(file='landscape.png')
    background_label2 = tkinter.Label(root2, image=background_image2)
    background_label2.place(relwidth=1, relheight=1)
    user_name_l = tkinter.Label(root2, text="User name", width=10, font=1000, bd=0)
    password_l = tkinter.Label(root2, text="Password", width=10, font=1000, bd=0)
    e = tkinter.Button(root2, text="Save question", command=lambda: input_database(user_name_e.get(), root2), bd=5, height=1 , width=20,font=1000)
    c = tkinter.Button(root2, text="Login", command=lambda: login(user_name_e.get(), password_e.get()), bd=5, height=1, width=20, font=1000)
    user_name_e = tkinter.Entry(root2, bd=5, width=20)
    password_e = tkinter.Entry(root2, bd=5, width=20, show='*')
    c.place(x=400, y=245)
    e.place(x=400, y=145)
    password_l.place(x=0, y=250)
    user_name_e.place(x=187, y=186)
    password_e.place(x=187, y=250)
    user_name_l.pack(side=tkinter.LEFT)
    p.pack()
    root2.mainloop()


def quitpage():
    top.quit()


def openpage():
    """Responsible for registration interface"""
    root = tkinter.Toplevel()
    top.withdraw()
    t = tkinter.Canvas(root, height=400, width=500)
    background_image1 = tkinter.PhotoImage(file='landscape.png')
    background_label1 = tkinter.Label(root, image=background_image1)
    background_label1.place(relwidth=1, relheight=1)
    user_name_e = tkinter.Entry(root, bd=5, width=20)
    password_e = tkinter.Entry(root, bd=5, width=20, show='*')
    user_name_l = tkinter.Label(root, text="User name", width=10, font=1000, bd=0)
    password_l = tkinter.Label(root, text="Password", width=10, font=1000, bd=0)
    user_type = tkinter.Checkbutton(root, text="Coordinator", variable=cor, onvalue=1, offvalue=0, height=1, width=10)
    user_type2 = tkinter.Checkbutton(root, text="Profsesor", variable=prof, onvalue=1, offvalue=0, height=1, width=10)
    user_type3 = tkinter.Checkbutton(root, text="Student", variable=stu, onvalue=1, offvalue=0, height=1, width=10)
    c = tkinter.Button(root, text="Complete registration", command=lambda: complete_register(user_name_e.get(), password_e.get(), cor.get(), prof.get(), stu.get()), bd=1, height=1, width=20, font=1000)

    c.place(x=300, y=300)
    password_l.place(x=0, y=150)
    user_name_e.place(x=187, y=86)
    password_e.place(x=187, y=150)
    user_type.place(x=0, y=250)
    user_type2.place(x=150, y=250)
    user_type3.place(x=300, y=250)
    user_name_l.place(x=0, y=86)
    t.pack()
    root.mainloop()


w = tkinter.Canvas(top, height=400, width=500)
# making a canvas for our gui
background_image = tkinter.PhotoImage(file='landscape.png')
background_label = tkinter.Label(top, image=background_image)
background_label.place(relwidth=1, relheight=1)
# putting an image on top of our page
A = tkinter.Button(top, text="Register", bd=5, height=2, width=20, font=10000,
                   command=lambda:  openpage())
B = tkinter.Button(top, text="Login ", command=lambda: openapage2(), bd=5, height=2, width=20, font=10000)
d = tkinter.Button(top, text="Exit", command=lambda: quitpage(), bd=5, height=2, width=20, font=10000)
# creating buttons
A.place(x=150, y=200)
B.place(x=150, y=130)
d.place(x=150, y=270)
w.pack()
# placements on the top page
top.mainloop()
