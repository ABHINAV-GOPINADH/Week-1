import tkinter as tk
from tkinter import messagebox

def check_palindrome():
    text = entry.get()
    if not text:
        messagebox.showwarning("Input Error", "Please enter a string.")
        return
    
    cleaned = ''.join(filter(str.isalnum, text)).lower()
    if cleaned == cleaned[::-1]:
        result_var.set("✅ It's a Palindrome!")
    else:
        result_var.set("❌ Not a Palindrome.")

# GUI setup
root = tk.Tk()
root.title("Palindrome Checker")
root.geometry("400x200")
root.configure(bg="#f0f8ff")

# Title label
title = tk.Label(root, text="Palindrome Checker", font=("Arial", 16, "bold"), bg="#f0f8ff", fg="#333")
title.pack(pady=10)

# Entry field
entry = tk.Entry(root, width=30, font=("Arial", 14))
entry.pack(pady=5)

# Check button
check_button = tk.Button(root, text="Check", font=("Arial", 12), command=check_palindrome, bg="#4caf50", fg="white")
check_button.pack(pady=10)

# Result label
result_var = tk.StringVar()
result_label = tk.Label(root, textvariable=result_var, font=("Arial", 14), bg="#f0f8ff", fg="#333")
result_label.pack(pady=5)

root.mainloop()
