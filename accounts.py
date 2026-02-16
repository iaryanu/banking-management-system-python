from datetime import date
from transaction import Transaction

class Account:
    next_account_number = 1000

    def __init__(self, name, pan, birth_date, password, initial_balance):
        self.account_number = self.generate_account_number()
        self.account_holder_name = name
        self.pan_number = pan
        self.birth_date = birth_date
        self.password = password
        self.balance = initial_balance
        self.transaction_history = []

        if initial_balance > 0:
            self.add_transaction(initial_balance, "DEPOSIT")

    @classmethod
    def generate_account_number(cls):
        acc = f"ACC{cls.next_account_number}"
        cls.next_account_number += 1
        return acc

    def validate_password(self, input_password):
        return self.password == input_password

    def change_password(self, new_password):
        self.password = new_password

    def withdraw(self, amount):
        if amount <= 0 or amount > self.balance:
            return False
        self.balance -= amount
        self.add_transaction(-amount, "WITHDRAWAL")
        return True

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.add_transaction(amount, "DEPOSIT")

    def add_transaction(self, amount, t_type):
        self.transaction_history.append(Transaction(amount, t_type))

    def get_transaction_history(self):
        return list(self.transaction_history)

    def get_age(self):
        today = date.today()
        return today.year - self.birth_date.year - (
            (today.month, today.day) < (self.birth_date.month, self.birth_date.day)
        )

    def __str__(self):
        return f"Account: {self.account_number} | Name: {self.account_holder_name} | Balance: ₹{self.balance:.2f}"
