
from datetime import datetime
from bank import Bank

bank = Bank()


def read_int_in_range(min_val, max_val):
    while True:
        try:
            val = int(input("> "))
            if min_val <= val <= max_val:
                return val
            print(f"* Enter number between {min_val}-{max_val}")
        except ValueError:
            print("* Enter valid number")


def read_float(min_val):
    while True:
        try:
            val = float(input("> "))
            if val >= min_val:
                return val
            print(f" * Enter amount >= {min_val}")
        except ValueError:
            print(" * Enter valid number")


import re

def create_account_menu():

    while True:
        name = input(" * Name: ")
        if re.fullmatch(r"[A-Za-z ]+", name):
            break
        print(" * Invalid, should be in format: letters only")

    while True:
        pan = input(" * PAN (ABCDE1234F): ").upper()
        if re.fullmatch(r"[A-Z]{5}[0-9]{4}[A-Z]", pan):
            break
        print(" * Invalid, should be in format: ABCDE1234F")

    while True:
        dob_str = input(" * Birth Date (yyyy-mm-dd): ")
        try:
            birth_date = datetime.strptime(dob_str, "%Y-%m-%d").date()
            break
        except ValueError:
            print(" * Invalid, should be in format: yyyy-mm-dd")


    while True:
        password = input(" * Password (6 digits): ")
        if re.fullmatch(r"\d{6}", password):
            break
        print(" * Invalid, should be exactly 6 digits")

    while True:
        try:
            initial = float(input(" * Initial Deposit: "))
            if initial >= 0:
                break
            print(" * Invalid, amount must be >= 0")
        except ValueError:
            print(" * Invalid number")

    bank.create_account(name, pan, birth_date, password, initial)



def login_and_operate():
    attempts = 0

    while attempts < 3:
        acc_num = input(" * Account Number: ")
        password = input(" * Password: ")

        account = bank.find_account(acc_num, password)

        if account:
            print(f" * Welcome {account.account_holder_name}")
            show_account_menu(account)
            return

        attempts += 1
        print(f" * Invalid account or password ({attempts}/3)")

    print(" * Too many failed attempts. Returning to main menu.")



def show_account_menu(account):
    while True:
        print(f"\n{account.account_number} (Balance: ₹{account.balance:.2f})")
        print("* 1. Deposit")
        print("* 2. Withdraw")
        print("* 3. Transfer")
        print("* 4. Change Password")
        print("* 5. Transaction History")
        print("* 6. Logout")

        choice = read_int_in_range(1, 6)

        if choice == 1:
            do_deposit(account)
        elif choice == 2:
            do_withdraw(account)
        elif choice == 3:
            do_transfer(account)
        elif choice == 4:
            change_password(account)
        elif choice == 5:
            show_history(account)
        elif choice == 6:
            print(" * Logged out.")
            return


def do_deposit(account):
    print(" * Amount:")
    amount = read_float(1)
    account.deposit(amount)
    print(" * Deposited successfully")


def do_withdraw(account):
    print(" * Amount:")
    amount = read_float(1)
    if account.withdraw(amount):
        print(" * Withdrawn successfully")
    else:
        print(" * Insufficient balance")


def do_transfer(from_account):
    to_acc = input(" * To Account Number: ")
    print(" * Amount:")
    amount = read_float(1)

    if bank.transfer(from_account.account_number, from_account.password, to_acc, amount):
        print("---Transfer successful---")


def change_password(account):
    new_pass = input(" * New Password: ")
    account.change_password(new_pass)
    print(" * Password changed successfully")


def show_history(account):
    history = account.get_transaction_history()
    if not history:
        print(" * No transactions yet")
        return

    print("\n * Transaction History:")
    for t in history:
        print(t)

def admin_panel():
    password = input(" * Enter admin password: ")

    if password != "Iadmin":
        print(" * Access denied")
        return

    print("* Admin access granted")
    bank.display_all_accounts()


def main_menu():
    print("* Welcome to Console Bank")

    while True:
        print("\nMain Menu")
        print("* 1. Create Account")
        print("* 2. Login & Operations")
        print("* 3. View All Accounts")
        print("* 4. Exit")

        choice = read_int_in_range(1, 4)

        if choice == 1:
            create_account_menu()
        elif choice == 2:
            login_and_operate()
        elif choice == 3:
            admin_panel()
        elif choice == 4:
            print("* Exiting......")
            break


if __name__ == "__main__":
    main_menu()

