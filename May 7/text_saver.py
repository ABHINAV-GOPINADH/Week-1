import tkinter as tk
from tkinter import messagebox

def save_to_file():
    filename = filename_entry.get().strip()
    text = text_entry.get("1.0", tk.END).strip()
    
    if not filename:
        messagebox.showwarning("Missing Filename", "Please enter a filename.")
        return
    if not text:
        messagebox.showwarning("Empty Text", "Please enter some text to save.")
        return

    try:
        with open(filename, "w", encoding="utf-8") as file:
            file.write(text)
        messagebox.showinfo("Success", f"Text saved to '{filename}'.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save file: {e}")

def read_from_file():
    filename = filename_entry.get().strip()
    
    if not filename:
        messagebox.showwarning("Missing Filename", "Please enter a filename.")
        return

    try:
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()
        text_entry.delete("1.0", tk.END)
        text_entry.insert(tk.END, content)
    except FileNotFoundError:
        messagebox.showerror("Error", f"'{filename}' not found.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to read file: {e}")

# GUI setup
root = tk.Tk()
root.title("Save & Read Text File")
root.geometry("550x450")
root.configure(bg="#f2f2f2")

tk.Label(root, text="Enter Filename:", bg="#f2f2f2", font=("Arial", 11)).pack(pady=5)
filename_entry = tk.Entry(root, font=("Arial", 11), width=40)
filename_entry.pack(pady=5)

tk.Label(root, text="Enter your text below:", bg="#f2f2f2", font=("Arial", 11)).pack(pady=5)
text_entry = tk.Text(root, width=60, height=15, font=("Arial", 10))
text_entry.pack(pady=5)

frame = tk.Frame(root, bg="#f2f2f2")
frame.pack(pady=10)

save_btn = tk.Button(frame, text="Save", width=15, bg="#4CAF50", fg="white", command=save_to_file)
save_btn.grid(row=0, column=0, padx=10)

read_btn = tk.Button(frame, text="Read", width=15, bg="#2196F3", fg="white", command=read_from_file)
read_btn.grid(row=0, column=1, padx=10)

root.mainloop()
