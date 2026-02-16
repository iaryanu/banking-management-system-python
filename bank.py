import re
from datetime import date
from accounts import Account

class Bank:
    def __init__(self):
        self.accounts = []

    def find_account(self, account_number, password):
        for acc in self.accounts:
            if acc.account_number == account_number and acc.validate_password(password):
                return acc
        return None

    def create_account(self, name, pan, birth_date, password, initial_balance):
        if birth_date > date(date.today().year - 18, date.today().month, date.today().day):
            print("Must be 18+ years old")
            return None

        if not self.is_valid_pan(pan):
            print("Invalid PAN format (ABCDE1234F)")
            return None

        new_account = Account(name, pan, birth_date, password, initial_balance)
        self.accounts.append(new_account)
        print(f"Account created: {new_account.account_number}")
        return new_account

    def transfer(self, from_acc_num, from_pass, to_acc_num, amount):
        from_acc = self.find_account(from_acc_num, from_pass)
        to_acc = next((a for a in self.accounts if a.account_number == to_acc_num), None)

        if not from_acc or not to_acc or amount <= 0 or amount > from_acc.balance:
            print("Transfer failed: Invalid accounts or insufficient balance")
            return False

        from_acc.withdraw(amount)
        to_acc.deposit(amount)
        print(f"Transfer successful: ₹{amount} from {from_acc_num} to {to_acc_num}")
        return True

    def is_valid_pan(self, pan):
        return re.fullmatch(r"[A-Z]{5}[0-9]{4}[A-Z]", pan) is not None

    def display_all_accounts(self):
        if not self.accounts:
            print("No accounts exist")
            return

        print("\nAll Accounts:")
        for acc in self.accounts:
            print(acc)
