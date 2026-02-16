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
