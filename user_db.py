import sqlite3

conn = sqlite3.connect('users.db')
cur = conn.cursor()


def create_table():
    """Creates a table only if doesn't exists"""
    with conn:
        cur.execute("""CREATE TABLE IF NOT EXISTS usersDB
                  (user_type TEXT NOT NULL,
                   user_name TEXT PRIMARY KEY,
                   user_password TEXT)""")


def insert_data(user_type, user_name, user_password):
    try:
        with conn:
            cur.execute("""INSERT INTO usersDB VALUES (?, ?, ?)""", (user_type, user_name, user_password))
    except sqlite3.IntegrityError:
        return "The user name is taken, please enter another one.\n"
    except:
        return "The insert failed.\n"


def get_data(user_name):
    cur.execute("""SELECT * FROM usersDB WHERE user_name=?""", (user_name,))
    return cur.fetchone()


def delete_user(user_name):
    with conn:
        cur.execute("""DELETE FROM usersDB WHERE user_name=?""", (user_name,))


def update_user_type(user_name, new_user_type):
    with conn:
        cur.execute("""UPDATE usersDB SET user_type=? WHERE user_name=?""", (new_user_type, user_name))


def update_user_name(user_name, new_user_name):
    with conn:
        cur.execute("""UPDATE usersDB SET user_name=? WHERE user_name=?""", (new_user_name, user_name))


def update_user_password(user_name, new_user_password):
    with conn:
        cur.execute("""UPDATE usersDB SET user_password=? WHERE user_name=?""", (new_user_password, user_name))
