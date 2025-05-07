import tkinter as tk
from tkinter import messagebox
import json
import os

contacts = {}

def add_contact():
    name = name_entry.get().strip()
    phone = phone_entry.get().strip()
    
    if not name or not phone:
        messagebox.showwarning("Missing Info", "Name and phone number are required.")
        return
    
    contacts[name] = {"phone": phone}
    messagebox.showinfo("Contact Added", f"{name} has been added.")
    clear_entries()
    update_display()

def save_contacts():
    try:
        with open("contacts.json", "w", encoding="utf-8") as f:
            json.dump(contacts, f, indent=4)
        messagebox.showinfo("Saved", "Contacts saved to 'contacts.json'.")
    except Exception as e:
        messagebox.showerror("Error", f"Could not save file:\n{e}")

def load_contacts():
    global contacts
    if not os.path.exists("contacts.json"):
        messagebox.showwarning("File Not Found", "No contacts.json file found.")
        return
    try:
        with open("contacts.json", "r", encoding="utf-8") as f:
            contacts = json.load(f)
        update_display()
        messagebox.showinfo("Loaded", "Contacts loaded from file.")
    except Exception as e:
        messagebox.showerror("Error", f"Could not load file:\n{e}")

def update_display():
    display_box.delete("1.0", tk.END)
    for name, info in contacts.items():
        display_box.insert(tk.END, f"Name: {name}\nPhone: {info['phone']}\n\n")

def clear_entries():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)

# GUI Setup
root = tk.Tk()
root.title("Contact Book")
root.geometry("500x450")
root.configure(bg="#f9f9f9")

tk.Label(root, text="Name:", bg="#f9f9f9").pack(pady=5)
name_entry = tk.Entry(root, width=40)
name_entry.pack(pady=2)

tk.Label(root, text="Phone:", bg="#f9f9f9").pack(pady=5)
phone_entry = tk.Entry(root, width=40)
phone_entry.pack(pady=2)

btn_frame = tk.Frame(root, bg="#f9f9f9")
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Add Contact", command=add_contact, bg="#4CAF50", fg="white", width=15).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Save Contacts", command=save_contacts, bg="#2196F3", fg="white", width=15).grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="Load Contacts", command=load_contacts, bg="#FF9800", fg="white", width=15).grid(row=0, column=2, padx=5)

tk.Label(root, text="Contacts List:", bg="#f9f9f9", font=("Arial", 12, "bold")).pack(pady=5)
display_box = tk.Text(root, width=60, height=15)
display_box.pack(pady=5)

root.mainloop()
    