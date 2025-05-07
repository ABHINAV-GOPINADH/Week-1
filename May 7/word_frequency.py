import tkinter as tk
from tkinter import messagebox, scrolledtext
from collections import Counter
import string

def count_word_frequency():
    filename = entry.get().strip()
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read().lower()
            text = text.translate(str.maketrans('', '', string.punctuation))
            words = text.split()
            word_counts = Counter(words)

            result_text.delete(1.0, tk.END)  # Clear previous result
            for word, count in word_counts.items():
                result_text.insert(tk.END, f"{word}: {count}\n")
    except FileNotFoundError:
        messagebox.showerror("File Not Found", f"'{filename}' does not exist.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# GUI setup
root = tk.Tk()
root.title("Word Frequency Counter")
root.geometry("500x500")
root.configure(bg="#f2f2f2")

label = tk.Label(root, text="Enter file name:", font=("Arial", 12), bg="#f2f2f2")
label.pack(pady=10)

entry = tk.Entry(root, width=40, font=("Arial", 12))
entry.pack(pady=5)

btn = tk.Button(root, text="Count Words", command=count_word_frequency, font=("Arial", 12), bg="#4CAF50", fg="white")
btn.pack(pady=10)

result_text = scrolledtext.ScrolledText(root, width=60, height=20, font=("Courier", 10))
result_text.pack(pady=10)

root.mainloop()
