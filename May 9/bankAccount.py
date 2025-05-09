from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLineEdit,
    QPushButton, QLabel, QMessageBox
)
import sys

class BankAccount:
    def __init__(self, owner, initial_balance=0):
        self.owner = owner
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited ₹{amount}. New balance: ₹{self.balance}"
        return "Deposit amount must be positive."

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds."
        elif amount <= 0:
            return "Withdrawal amount must be positive."
        else:
            self.balance -= amount
            return f"Withdrew ₹{amount}. New balance: ₹{self.balance}"

    def get_balance(self):
        return self.balance


class BankApp(QWidget):
    def __init__(self):
        super().__init__()
        self.account = BankAccount("User", 0)
        self.setWindowTitle("Bank Account")

        self.layout = QVBoxLayout()

        self.info_label = QLabel("Enter amount to deposit or withdraw")
        self.layout.addWidget(self.info_label)

        self.amount_input = QLineEdit()
        self.amount_input.setPlaceholderText("Enter amount")
        self.layout.addWidget(self.amount_input)

        self.deposit_btn = QPushButton("Deposit")
        self.deposit_btn.clicked.connect(self.deposit)
        self.layout.addWidget(self.deposit_btn)

        self.withdraw_btn = QPushButton("Withdraw")
        self.withdraw_btn.clicked.connect(self.withdraw)
        self.layout.addWidget(self.withdraw_btn)

        self.balance_btn = QPushButton("Check Balance")
        self.balance_btn.clicked.connect(self.check_balance)
        self.layout.addWidget(self.balance_btn)

        self.setLayout(self.layout)

    def get_amount(self):
        try:
            return float(self.amount_input.text())
        except ValueError:
            QMessageBox.warning(self, "Invalid input", "Please enter a valid number.")
            return None

    def deposit(self):
        amount = self.get_amount()
        if amount is not None:
            msg = self.account.deposit(amount)
            QMessageBox.information(self, "Deposit", msg)

    def withdraw(self):
        amount = self.get_amount()
        if amount is not None:
            msg = self.account.withdraw(amount)
            QMessageBox.information(self, "Withdraw", msg)

    def check_balance(self):
        balance = self.account.get_balance()
        QMessageBox.information(self, "Balance", f"Current balance: ₹{balance}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BankApp()
    window.resize(300, 200)
    window.show()
    sys.exit(app.exec())
