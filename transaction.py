from datetime import datetime

class Transaction:
    def __init__(self, amount, t_type):
        self.timestamp = datetime.now()
        self.amount = amount
        self.type = t_type

    def __str__(self):
        return f"[{self.timestamp.strftime('%d-%m-%Y %H:%M')}] {self.type}: ₹{self.amount:.2f}"

    def get_amount(self):
        return self.amount

    def get_type(self):
        return self.type

    def get_timestamp(self):
        return self.timestamp
