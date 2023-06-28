'''
Project Description: Create a bank account management system that allows users to create and manage 
their bank accounts. The system should allów users to perform basic banking operations
like depositing and withdrawing money, checking balance, and viewing transaction history.

Steps to Implement:

1. Create a BankAcount class that will have the following attributes: account number, account holder name, 
account type (Savings or Checking), and balance.
2. Define a constructor method that will initialize the account attributes when a new object is created.
3. Define methods for depositing and withdrawing money from the account. These methods should update 
the balance attribute accordingly.
4. Define a method for checking the current balance of the account.
5. Define a method for displaying the transaction history of the account.
6. Create a main function that will allow users to create new accounts and perform banking 
operations on their accounts.

'''


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
            self.transaction_history.append(f"{self.account_holder_name} deposited {amount} naira")
            return f"${amount} Deposited"

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient Funds"
        self.balance -= amount
        self.transaction_history.append(f"{self.account_holder_name} withdrew {amount} naira")
        return f"${amount} Withdrawn"

    def check_balance(self):
        if self.account_holder_name and self.account_number:
            return f"Your account balance: {self.balance}"
        else:
            return f"Invalid Credentials"

    def display_transaction_history(self):
        # for transaction in self.transaction_history:
        #     print(transaction)
        with open(f"transaction_history.txt", "r") as file:
            result = file.read()
        return result

    def add_transaction(self, message):
            with open("transaction_history.txt", "a") as file:
                file.write(f"{message}\n")

def main():
    accounts = []

    while True:
        print("Bank Management System")
        print("1. Create a new bank account")
        print("2. Deposit funds to your account")
        print("3. Withdraw funds from your account")
        print("4. Check your balance")
        print("5. Display transaction history")
        response = input("")

        if response == "1":
            name = input("Enter your name: ")
            account_type = input("Enter account type (Savings/Checking): ")
            account_number = input("Enter account number: ")
            new_account = BankAccount(account_number, name, account_type)
            accounts.append(new_account)
            print("Account created successfully!")

        elif response == "2":
            name = input("Enter your name: ")
            for account in accounts:
                if account.account_holder_name == name:
                    amount = int(input("Please enter amount: "))
                    print(account.deposit(amount))
                    break
            else:
                print("Can't find your account.")

        elif response == "3":
            name = input("Enter your name: ")
            for account in accounts:
                if account.account_holder_name == name:
                    amount = int(input("Please enter amount: "))
                    print(account.withdraw(amount))
                    break
            else:
                print("Can't find your account.")

        elif response == "4":
            name = input("Enter your name: ")
            for account in accounts:
                if account.account_holder_name == name:
                    print("Your account balance:", account.check_balance())
                    break
            else:
                print("Can't find your account.")
        
        elif response == "5":
            name = input("Enter your name: ")
            for account in accounts:
                if account.account_holder_name == name:
                    account.display_transaction_history()
                    print("Your transaction history:", account.transaction_history)
                    break
            else:
                print("Can't find your account.")


main()






