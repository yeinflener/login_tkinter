import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("LOGIN FORM")
window.geometry('650x450')
window.configure(bg="#333333")

def login():
    username = "Mary Beth"
    password = "12345"
    if username_entry.get() == username and password_entry.get() == password:
        messagebox.showinfo(title="Login Success", message="You successfully logged in.")
    else:
        messagebox.showinfo(title="Error", message="Invalid login.")
        print("Invalid login")

frame = tk.Frame(bg='#333333')
# Creating widgets
login_label = tk.Label(frame, text='Login', bg='#333333', fg= "#34cf21", font=("Arial", 30))
username_label = tk.Label(frame, text="Username", bg='#333333', fg="#FFFFFF", font=("Arial", 14))
username_entry = tk.Entry(frame, font=("Arial", 16), bg="#c5ffbd")
password_entry = tk.Entry(frame, show="*", font=("Arial", 16), bg="#c5ffbd")
password_label = tk.Label(frame, text="Password", bg='#333333', fg="#FFFFFF", font=("Arial", 14))
login_button = tk.Button(frame, text="Login", bg="#34cf21", fg="#FFFFFF", font=("Arial", 18), command=login)

# Placing widgets on the screen
login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady = 40)
username_label.grid(row=1, column=0)
username_entry.grid(row=1, column=1, pady=20)
password_label.grid(row=2, column=0)
password_entry.grid(row=2, column=1, pady=20)
login_button.grid(row=3, column=0,  columnspan=2, pady = 25)

frame.pack()

window.mainloop()
print("hi")