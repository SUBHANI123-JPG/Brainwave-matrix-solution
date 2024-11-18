class ATM:
    def _init_(self):
        self.balance = 1000  # Default balance
        self.pin = "1234"  # Default PIN

    def start(self):
        print("Welcome to the ATM!")
        attempts = 3
        while attempts > 0:
            entered_pin = input("Enter your 4-digit PIN: ")
            if entered_pin == self.pin:
                print("Login successful.")
                self.menu()
                break
            else:
                attempts -= 1
                print(f"Invalid PIN. You have {attempts} attempts left.")
        else:
            print("Too many incorrect attempts. Exiting...")

    def menu(self):
        while True:
            print("\n--- ATM Menu ---")
            print("1. Balance Inquiry")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Change PIN")
            print("5. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.balance_inquiry()
            elif choice == "2":
                self.deposit()
            elif choice == "3":
                self.withdraw()
            elif choice == "4":
                self.change_pin()
            elif choice == "5":
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

    def balance_inquiry(self):
        print(f"Your current balance is: ${self.balance:.2f}")

    def deposit(self):
        try:
            amount = float(input("Enter amount to deposit: "))
            if amount > 0:
                self.balance += amount
                print(f"${amount:.2f} deposited successfully. New balance: ${self.balance:.2f}")
            else:
                print("Deposit amount must be positive.")
        except ValueError:
            print("Invalid input. Please enter a valid amount.")

    def withdraw(self):
        try:
            amount = float(input("Enter amount to withdraw: "))
            if amount > 0:
                if amount <= self.balance:
                    self.balance -= amount
                    print(f"${amount:.2f} withdrawn successfully. Remaining balance: ${self.balance:.2f}")
                else:
                    print("Insufficient funds.")
            else:
                print("Withdrawal amount must be positive.")
        except ValueError:
            print("Invalid input. Please enter a valid amount.")

    def change_pin(self):
        current_pin = input("Enter your current PIN: ")
        if current_pin == self.pin:
            new_pin = input("Enter your new 4-digit PIN: ")
            confirm_pin = input("Confirm your new PIN: ")
            if new_pin == confirm_pin and len(new_pin) == 4 and new_pin.isdigit():
                self.pin = new_pin
                print("PIN changed successfully.")
            else:
                print("PINs do not match or invalid PIN format.")
        else:
            print("Incorrect current PIN.")

if __name__== "_main_":
    atm = ATM()
    atm.start()
