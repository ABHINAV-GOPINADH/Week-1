import tkinter as tk
from tkinter import ttk, messagebox

def celsius_to_fahrenheit():
    try:
        c = float(temp_entry.get())
        f = (c * 9/5) + 32
        result_var.set(f"{c} °C = {f:.2f} °F")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number")

def fahrenheit_to_celsius():
    try:
        f = float(temp_entry.get())
        c = (f - 32) * 5/9
        result_var.set(f"{f} °F = {c:.2f} °C")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number")

# GUI Setup
root = tk.Tk()
root.title("🌡️ Temperature Converter")
root.geometry("350x250")
root.config(bg="#f0f0f0")

tk.Label(root, text="Enter Temperature:", font=("Arial", 12), bg="#f0f0f0").pack(pady=10)
temp_entry = ttk.Entry(root, font=("Arial", 12))
temp_entry.pack(pady=5)

ttk.Button(root, text="Convert to Fahrenheit", command=celsius_to_fahrenheit).pack(pady=5)
ttk.Button(root, text="Convert to Celsius", command=fahrenheit_to_celsius).pack(pady=5)

result_var = tk.StringVar()
result_label = tk.Label(root, textvariable=result_var, font=("Arial", 12, "bold"), bg="#f0f0f0", fg="green")
result_label.pack(pady=20)

root.mainloop()
