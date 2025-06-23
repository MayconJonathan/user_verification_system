import sqlite3
import hashlib
import tkinter as tk
from tkinter import messagebox

def create_user_table():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (username TEXT, password TEXT)''')
    conn.commit()
    conn.close()

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register():
    user = entry_user.get()
    pwd = hash_password(entry_pass.get())
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (user, pwd))
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "User registered!")

def login():
    user = entry_user.get()
    pwd = hash_password(entry_pass.get())
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username=? AND password=?", (user, pwd))
    if c.fetchone():
        messagebox.showinfo("Success", "Login successful!")
    else:
        messagebox.showerror("Error", "Invalid credentials")
    conn.close()

# GUI
root = tk.Tk()
root.title("Login System")

tk.Label(root, text="Username").pack()
entry_user = tk.Entry(root)
entry_user.pack()

tk.Label(root, text="Password").pack()
entry_pass = tk.Entry(root, show="*")
entry_pass.pack()

tk.Button(root, text="Register", command=register).pack()
tk.Button(root, text="Login", command=login).pack()

create_user_table()
root.mainloop()
