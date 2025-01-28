import getpass

class ATM:
    def __init__(self):
        
        self.accounts = {
            "123456": ["1234", 5000.0, []],
            "654321": ["4321", 10000.0, []]
        }
        self.current_user = None

    def authenticate_user(self):
        account_number = input("Enter your account number: ")
        if account_number in self.accounts:
            try:
                # Attempt secure input using getpass
                pin = getpass.getpass("Enter your PIN: ")
            except Exception:
                # Fallback to input() if getpass fails
                print("Secure input not available. Using standard input.")
                pin = input("Enter your PIN: ")
            
            if pin == self.accounts[account_number][0]:
                self.current_user = account_number
                print("Login successful!")
                return True
            else:
                print("Incorrect PIN.")
        else:
            print("Account number not found.")
        return False

    def check_balance(self):
        balance = self.accounts[self.current_user][1]
        print(f"Your current balance is: ₹{balance:.2f}")

    def deposit(self):
        try:
            amount = float(input("Enter the amount to deposit: ₹"))
            if amount > 0:
                self.accounts[self.current_user][1] += amount
                self.accounts[self.current_user][2].append(f"Deposited: ₹{amount:.2f}")
                print(f"₹{amount:.2f} deposited successfully.")
                self.check_balance()
            else:
                print("Deposit amount must be positive.")
        except ValueError:
            print("Invalid amount. Please enter a numeric value.")

    def withdraw(self):
        try:
            amount = float(input("Enter the amount to withdraw: ₹"))
            balance = self.accounts[self.current_user][1]
            if amount > 0 and amount <= balance:
                self.accounts[self.current_user][1] -= amount
                self.accounts[self.current_user][2].append(f"Withdrew: ₹{amount:.2f}")
                print(f"₹{amount:.2f} withdrawn successfully.")
                self.check_balance()
            elif amount > balance:
                print("Insufficient funds.")
            else:
                print("Withdrawal amount must be positive.")
        except ValueError:
            print("Invalid amount. Please enter a numeric value.")

    def transaction_history(self):
        history = self.accounts[self.current_user][2]
        if history:
            print("\nTransaction History:")
            for transaction in history:
                print(transaction)
        else:
            print("No transactions found.")

    def logout(self):
        print("Logging out...")
        self.current_user = None

    def menu(self):
        while True:
            print("\n--- ATM Interface ---")
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Transaction History")
            print("5. Logout")
            
            try:
                choice = int(input("Enter your choice: "))
                if choice == 1:
                    self.check_balance()
                elif choice == 2:
                    self.deposit()
                elif choice == 3:
                    self.withdraw()
                elif choice == 4:
                    self.transaction_history()
                elif choice == 5:
                    self.logout()
                    break
                else:print("Invalid choice. Please try again.")
            except ValueError:
                print("Please enter a valid number.")


def main():
    atm = ATM()
    print("Welcome to the ATM!")
    if atm.authenticate_user():
        atm.menu()
    else:
        print("Authentication failed. Exiting...")

if __name__ == "__main__":
    main()