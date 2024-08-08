class ATMMachine:
    def __init__(self, pin):
        self.balance = 0
        self.pin = pin
        self.transaction_history = []

    def check_pin(self):
        entered_pin = input("Enter your PIN: ")
        if entered_pin == self.pin:
            return True
        else:
            print("Incorrect PIN.")
            return False

    def account_balance_inquiry(self):
        if self.check_pin():
            print(f"Your current balance is: ${self.balance:.2f}")
            self.transaction_history.append("Balance inquiry")
        else:
            print("PIN verification failed. Cannot perform balance inquiry.")

    def cash_withdrawal(self):
        if self.check_pin():
            amount = float(input("Enter amount to withdraw: $"))
            if amount > self.balance:
                print("Insufficient balance.")
            else:
                self.balance -= amount
                self.transaction_history.append(f"Withdrew ${amount:.2f}")
                print(f"${amount:.2f} withdrawn successfully.")
        else:
            print("PIN verification failed. Cannot perform cash withdrawal.")

    def cash_deposit(self):
        if self.check_pin():
            amount = float(input("Enter amount to deposit: $"))
            self.balance += amount
            self.transaction_history.append(f"Deposited ${amount:.2f}")
            print(f"${amount:.2f} deposited successfully.")
        else:
            print("PIN verification failed. Cannot perform cash deposit.")

    def change_pin(self):
        if self.check_pin():
            new_pin = input("Enter your new PIN: ")
            self.pin = new_pin
            self.transaction_history.append("PIN changed")
            print("PIN changed successfully.")
        else:
            print("PIN verification failed. Cannot change PIN.")

    def show_transaction_history(self):
        print("Transaction History:")
        for transaction in self.transaction_history:
            print(transaction)

    def start(self):
        while True:
            print("\n1. Account Balance Inquiry")
            print("2. Cash Withdrawal")
            print("3. Cash Deposit")
            print("4. Change PIN")
            print("5. Transaction History")
            print("6. Exit")

            choice = input("Choose an option: ")

            if choice == '1':
                self.account_balance_inquiry()
            elif choice == '2':
                self.cash_withdrawal()
            elif choice == '3':
                self.cash_deposit()
            elif choice == '4':
                self.change_pin()
            elif choice == '5':
                self.show_transaction_history()
            elif choice == '6':
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

# Example usage
atm = ATMMachine(pin="1234")
atm.start()
