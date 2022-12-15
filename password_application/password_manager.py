from tkinter import *
import sqlite3

manager_screen = Tk()
manager_screen.title("Password Manager")
width = 400
height = 300
screen_width = manager_screen.winfo_screenwidth()  # Width of the screen
screen_height = manager_screen.winfo_screenheight()  # Height of the screen
x = (screen_width / 2) - (width / 2)
y = (screen_height / 2) - (height / 2)
manager_screen.geometry("%dx%d+%d+%d" % (width, height, x, y))


conn = sqlite3.connect("passmanager.db")
cursor = conn.cursor()
cursor.execute("""
                CREATE TABLE IF NOT EXISTS manager (
                website NOT NULL, 
                url NOT NULL, 
                id NOT NULL, 
                password NOT NULL)""")
conn.commit()
conn.close()


def submit_new():
    conn = sqlite3.connect("passmanager.db")
    cursor = conn.cursor()


def change_to_add():
    manager_screen.title("Add New Query")
    main_menu.forget()
    update_frame.forget()
    query_frame.forget()
    add_frame.pack(fill="both", expand=1)


def change_to_update():
    manager_screen.title("Update Query")
    main_menu.forget()
    add_frame.forget()
    query_frame.forget()
    update_frame.pack(fill="both", expand=1)


def change_to_query():
    manager_screen.title("Show Info")
    main_menu.forget()
    add_frame.forget()
    update_frame.forget()
    query_frame.pack(fill="both", expand=1)


def change_to_main():
    manager_screen.title("Password Manager")
    query_frame.forget()
    add_frame.forget()
    update_frame.forget()
    main_menu.pack(fill="both", expand=1)


main_menu = Frame(manager_screen)
add_frame = Frame(manager_screen)
update_frame = Frame(manager_screen)
query_frame = Frame(manager_screen)


Label(main_menu, text="Welcome!", font=25).pack()
Label(main_menu, text="").pack()
Button(main_menu, text="Add New Record", height="2", width="30", command=change_to_add).pack()
Label(main_menu, text="").pack()
Button(main_menu, text="Update Record", height="2", width="30", command=change_to_update).pack()
Label(main_menu, text="").pack()
Button(main_menu, text="Show All Records", height="2", width="30", command=change_to_query).pack()


Label(add_frame, text="Add New Record", font=25).pack()
Label(add_frame, text="Website/App").pack()
web_name = Entry(add_frame)
web_name.pack()
Label(add_frame, text="URL").pack()
url_name = Entry(add_frame)
url_name.pack()
Label(add_frame, text="Username/ID").pack()
user_id = Entry(add_frame)
user_id.pack()
Label(add_frame, text="Password").pack()
password = Entry(add_frame)
password.pack()
Button(add_frame, text="Add").pack()
Button(add_frame, text="Back To Main", command=change_to_main).pack()


Label(update_frame, text="Update Record", font=25).pack()
Label(update_frame, text="Website/App to Update")
site_app = Entry(update_frame)
site_app.pack()
Label(update_frame, text="New Username/ID").pack()
new_user_id = Entry(update_frame)
new_user_id.pack()
Label(update_frame, text="New Password").pack()
new_pass = Entry(update_frame)
new_pass.pack()
Button(update_frame, text="Update").pack()
Button(update_frame, text="Back To Main", command=change_to_main).pack()


main_menu.pack(fill='both', expand=1)


def main():
    manager_screen.mainloop()


if __name__ == "__main__":
    main()