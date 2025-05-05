import tkinter as tk

def validate_input():
    try:
        # Try to convert inputs to float
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        return num1, num2
    except ValueError:
        # Return None if input is invalid
        result_var.set("Error! Please enter valid numbers.")
        return None, None

def add():
    num1, num2 = validate_input()
    if num1 is None or num2 is None:
        return  # If validation fails, return early and do nothing
    result_var.set(num1 + num2)

def subtract():
    num1, num2 = validate_input()
    if num1 is None or num2 is None:
        return
    result_var.set(num1 - num2)

def multiply():
    num1, num2 = validate_input()
    if num1 is None or num2 is None:
        return
    result_var.set(num1 * num2)

def divide():
    num1, num2 = validate_input()
    if num1 is None or num2 is None:
        return
    if num2 == 0:
        result_var.set("Error! Division by zero.")
    else:
        result_var.set(num1 / num2)

# Create main window
window = tk.Tk()
window.title("Simple Calculator")
window.geometry("400x300")  # Set the window size
window.config(bg="#2c3e50")  # Background color of window

# Create input fields
entry1 = tk.Entry(window, width=15, font=("Arial", 14), bd=5, relief="solid", justify="right")
entry1.grid(row=0, column=0, padx=10, pady=10)

entry2 = tk.Entry(window, width=15, font=("Arial", 14), bd=5, relief="solid", justify="right")
entry2.grid(row=0, column=1, padx=10, pady=10)

# Create result label
result_var = tk.StringVar()
result_label = tk.Label(window, textvariable=result_var, font=("Arial", 14), bg="#34495e", fg="white", width=30, height=2)
result_label.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Create buttons for operations with styling
button_style = {
    'width': 10, 
    'height': 2, 
    'font': ("Arial", 14), 
    'bd': 5, 
    'relief': "raised", 
    'bg': "#2980b9", 
    'fg': "white",
    'activebackground': "#3498db",
    'activeforeground': "white"
}

button_add = tk.Button(window, text="Add", **button_style, command=add)
button_add.grid(row=2, column=0, padx=10, pady=10)

button_subtract = tk.Button(window, text="Subtract", **button_style, command=subtract)
button_subtract.grid(row=2, column=1, padx=10, pady=10)

button_multiply = tk.Button(window, text="Multiply", **button_style, command=multiply)
button_multiply.grid(row=3, column=0, padx=10, pady=10)

button_divide = tk.Button(window, text="Divide", **button_style, command=divide)
button_divide.grid(row=3, column=1, padx=10, pady=10)

# Run the main loop
window.mainloop()
