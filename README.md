#  Python Mini Projects – Week 1

## May 5
This repository includes three beginner-friendly Python programs for practice in GUI and console-based applications using Python.

###  1. Simple Calculator (Tkinter GUI)

A basic calculator that supports arithmetic operations (addition, subtraction, multiplication, and division).

**Features:**
- Built using `tkinter`.
- Input validation (handles empty or invalid input).
- Real-time result display.
- Colorful and clean GUI.

**How to Run:**
```bash
python calculator.py
```
 ### 2. Number Guessing Game (Tkinter GUI)
A fun number guessing game where the user guesses a randomly generated number between 1 and 100.

**Features:**
- Random number generation.
- Feedback on each guess (too high, too low, or correct).
- Tracks the number of attempts.
- Handles invalid (non-numeric) inputs.
- Option to start a new game.

**How to Run:**
```bash
python guessing_game.py
```
###3. Fibonacci Sequence Generator
A program that generates and prints the Fibonacci sequence up to a user-specified number of terms.

**Features:**
- User input for number of terms.
- Validates positive integer input.
- Generates and displays the Fibonacci sequence.

**How to Run:**
```bash
python fibonacci.py
```
## May 6

### 1. Palindrome Checker

This project implements a program that checks whether a given string or number is a palindrome. A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward (ignoring spaces, punctuation, and capitalization).

**Features:**
- Checks if the input string is a palindrome.
- Handles both string and numeric inputs.
- Ignores spaces, punctuation, and case when checking for a palindrome.

**How to Run:**

  ```bash
  python palindrome.py
  ```
### 2. Login System

This project implements a simple login system using Python. Users can register and log in with a username and password. The system stores user credentials in a local file and verifies the login details upon login attempt.

**Features:**
- Allows users to register with a username and password.
- Saves user credentials securely in a file.
- Allows users to log in using the username and password.

**How to Run:**

  ```bash
  python login.py
  ```
### 3. Temperature Converter

This project converts temperature values between Celsius, Fahrenheit, and Kelvin. It provides an easy-to-use interface to enter a temperature and choose the desired conversion unit.

**Features:**
- Converts Celsius to Fahrenheit and Kelvin.
- Converts Fahrenheit to Celsius and Kelvin.
- Converts Kelvin to Celsius and Fahrenheit.

**How to Run:**

  ```bash
  python temperature.py
  ```
## May 7

### 1. Word Frequency Counter

This GUI app reads a text file and counts how often each word appears.

**Features:**
- GUI input for file name.
- Reads file content and counts word frequency.
- Displays result in the GUI.

**How to Run:**

  ```bash
  python word_frequency.py
  ```
### 2. User Input Save & Read 

This app allows users to input text and a file name, then saves the input to the file and reads it back.

**Features:**
- Enter custom file name and content.
- Save input to a file.
- Read content from the same file.
- Simple Tkinter-based interface.

**How to Run:**

  ```bash
  python text_saver.py
  ```
### 3. Contact Book

A simple contact book application that lets you add, search, view, and delete contacts. It stores contact data (name and phone number) using a Python dictionary and saves/loads data from a JSON file.

**Features:**
- Add, search, and delete contacts.
- View all contacts.
- Data stored persistently using a JSON file.
- Clean GUI built with tkinter.

**How to Run:**

  ```bash
  python contact.py
  ```
## May 8

###  Sales Data Analysis

This project presents a Jupyter Notebook that performs exploratory data analysis (EDA) on sales data. The goal is to extract meaningful insights, visualize trends, and support data-driven business decisions.

#### Files

- `sales.ipynb`: Jupyter notebook containing the full analysis and visualizations.

#### Features

- Data cleaning and handling of missing values  
- Trend analysis using grouped data  
- Visualizations using `matplotlib`  
- Summary statistics and insights  

#### Technologies Used

- Python 3.x  
- Jupyter Notebook  
- Pandas  
- Matplotlib  
- NumPy  

## May 9

### 1. Bank Account GUI App (with PySide6)  

A simple desktop banking interface that simulates a bank account system using Object-Oriented Programming (OOP) and PySide6 for the GUI.

**Features:**

- User login with username and password
- Deposit money
- Withdraw money (with balance check)
- Display current balance
- Clean OOP-based code structure using Python classes

#### Technologies Used

- **Python 3.x** 
- **PySide6** 
- **Object-Oriented Programming (OOP)** 
---

**How to Run:**

  ```bash
  python bankAccount.py
  ```

### 1. Student Management System

A simple Student Management System implemented using Python and Object-Oriented Programming (OOP). This system allows you to add, remove, and search for student records through a basic interface.

**Features:**

- Add new student records
- Remove existing students by ID
- Search students by name or ID
- List all students
- Object-Oriented structure for easy extensibility

#### Technologies Used

- **PySide6** 
- **Object-Oriented Programming (OOP)** 
---

**How to Run:**

  ```bash
  python StudentManager.py
  ```

###  Streamlit Data Analysis App (OOP-Based)

This is a simple Streamlit-based data analysis tool that allows users to upload a CSV file, analyze its contents using object-oriented programming (OOP) design, and visualize numeric data through plots.

**Features:**

- Upload any `.csv` file
- View data preview and summary statistics
- Automatically detect numeric columns
- Calculate column-wise average
- Line plot and histogram visualization
- Clean and modular object-oriented design

#### Technologies Used

- **Streamlit** 
- **Pandas** 
- **Matplotlib** 
- **Object-Oriented Programming (OOP)** 

**How to Run:**

  ```bash
  python -m Analyze.py

  ```