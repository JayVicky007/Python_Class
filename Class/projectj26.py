class BankAccount:
    def __init__(self, account_number, account_holder_name, account_type, balance=0):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.account_type = account_type
        self.balance = balance
        self.transaction_history = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"You deposited: {amount}")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"You withdrew: {amount}")

    def check_balance(self):
        return self.balance

    def display_transaction_history(self):
        for transaction in self.transaction_history:
            print(transaction)


def main():
    accounts = []

    while True:
        print("Bank Account Management System")
        print("1. Create a new account")
        print("2. Access an existing account")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            account_number = input("Enter account number: ")
            account_holder_name = input("Enter account holder name: ")
            account_type = input("Enter account type (Savings or Checking): ")

            account = BankAccount(account_number, account_holder_name, account_type)
            accounts.append(account)

            print("Account created successfully!")
            print()

        elif choice == "2":
            account_number = input("Enter account number: ")
            account = None

            for acc in accounts:
                if acc.account_number == account_number:
                    account = acc
                    break

            if account is None:
                print("Account not found!")
                print()
            else:
                print("Account found!")
                print("1. Deposit")
                print("2. Withdraw")
                print("3. Check balance")
                print("4. Display transaction history")
                print("5. Back to main menu")

                option = input("Enter your option (1-5): ")

                if option == "1":
                    amount = float(input("Enter amount to deposit: "))
                    account.deposit(amount)
                    print("Amount deposited successfully!")
                    print()
                elif option == "2":
                    amount = float(input("Enter amount to withdraw: "))
                    account.withdraw(amount)
                    print("Amount withdrawn successfully!")
                    print()
                elif option == "3":
                    balance = account.check_balance()
                    print(f"Current balance: {balance}")
                    print()
                elif option == "4":
                    account.display_transaction_history()
                    print()
                elif option == "5":
                    continue

        elif choice == "3":
            break

        else:
            print("Invalid choice! Please try again.")
            print()


if __name__ == "__main__":
    main()
