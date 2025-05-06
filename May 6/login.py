import tkinter as tk
from tkinter import messagebox
import sqlite3
import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


# ----------------- DB SETUP -----------------
conn = sqlite3.connect("users.db")
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        username TEXT PRIMARY KEY,
        password TEXT NOT NULL
    )
""")
conn.commit()
conn.close()

# ----------------- MAIN WINDOW -----------------
root = tk.Tk()
root.title("Login System")
root.geometry("400x400")
root.config(bg="#F0F2F5")

# Common styles
font_title = ("Helvetica", 18, "bold")
font_label = ("Helvetica", 11)
bg_color = "#FFFFFF"
btn_color = "#4A90E2"
btn_fg = "#FFFFFF"
entry_bg = "#F7F7F7"

# ----------------- FRAME SWITCHING -----------------
frame_login = tk.Frame(root, bg=bg_color)
frame_signup = tk.Frame(root, bg=bg_color)
frame_home = tk.Frame(root, bg=bg_color)

def clear_entries():
    for frame in [frame_login, frame_signup]:
        for widget in frame.winfo_children():
            if isinstance(widget, tk.Entry):
                widget.delete(0, tk.END)

def show_frame(frame):
    for f in (frame_login, frame_signup, frame_home):
        f.pack_forget()
    frame.pack(pady=30)

# ----------------- FUNCTIONALITY -----------------
def login():
    username = login_username.get()
    password = login_password.get()
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    hashed_password = hash_password(password)
    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, hashed_password))
    result = cursor.fetchone()
    conn.close()
    if result:
        clear_entries()
        show_frame(frame_home)
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

def signup():
    username = signup_username.get()
    password = signup_password.get()
    if not username or not password:
        messagebox.showwarning("Input Error", "All fields are required")
        return
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    try:
        hashed_password = hash_password(password)
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
        conn.commit()
        messagebox.showinfo("Success", "Account created! You can now log in.")
        show_frame(frame_login)
    except sqlite3.IntegrityError:
        messagebox.showerror("Signup Failed", "Username already exists")
    conn.close()

# ----------------- LOGIN UI -----------------
tk.Label(frame_login, text="Login", font=font_title, bg=bg_color).pack(pady=10)
tk.Label(frame_login, text="Username", font=font_label, bg=bg_color).pack()
login_username = tk.Entry(frame_login, font=font_label, bg=entry_bg)
login_username.pack(pady=5, ipadx=30, ipady=5)

tk.Label(frame_login, text="Password", font=font_label, bg=bg_color).pack()
login_password = tk.Entry(frame_login, show="*", font=font_label, bg=entry_bg)
login_password.pack(pady=5, ipadx=30, ipady=5)

tk.Button(frame_login, text="Login", command=login, bg=btn_color, fg=btn_fg, font=font_label).pack(pady=10)
tk.Label(frame_login, text="Don't have an account?", bg=bg_color, font=font_label).pack()
tk.Button(frame_login, text="Sign Up", command=lambda: show_frame(frame_signup), bg="#DDD", font=font_label).pack(pady=5)

# ----------------- SIGNUP UI -----------------
tk.Label(frame_signup, text="Sign Up", font=font_title, bg=bg_color).pack(pady=10)
tk.Label(frame_signup, text="Username", font=font_label, bg=bg_color).pack()
signup_username = tk.Entry(frame_signup, font=font_label, bg=entry_bg)
signup_username.pack(pady=5, ipadx=30, ipady=5)

tk.Label(frame_signup, text="Password", font=font_label, bg=bg_color).pack()
signup_password = tk.Entry(frame_signup, show="*", font=font_label, bg=entry_bg)
signup_password.pack(pady=5, ipadx=30, ipady=5)

tk.Button(frame_signup, text="Create Account", command=signup, bg=btn_color, fg=btn_fg, font=font_label).pack(pady=10)
tk.Button(frame_signup, text="Back to Login", command=lambda: show_frame(frame_login), bg="#DDD", font=font_label).pack()

# ----------------- HOME PAGE -----------------
tk.Label(frame_home, text="🎉 Welcome to the Home Page!", font=font_title, bg=bg_color).pack(pady=40)
tk.Button(frame_home, text="Logout", command=lambda: show_frame(frame_login), bg=btn_color, fg=btn_fg, font=font_label).pack()

# Start the app
show_frame(frame_login)
root.mainloop()
