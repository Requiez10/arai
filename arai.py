class BankAccount:
    def __init__(self, account_number, owner, balance=0):
        self.account_number = account_number
        self.owner = owner
        self._bank_code = "123ABC"
        self.__pin = "0000"
        self.balance = balance

    def deposit(self, amount):
        """Adds money to the balance."""
        if amount > 0:
            self.balance += amount
            print(f"\nDeposited ₱{amount:.2f}. New balance: ₱{self.balance:.2f}")
        else:
            print("\nDeposit amount must be positive.")

    def withdraw(self, amount):
        """Deducts money if the balance is sufficient."""
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"\nWithdrew ₱{amount:.2f}. New balance: ₱{self.balance:.2f}")
            else:
                print("\nInsufficient balance for this withdrawal.")
        else:
            print("\nWithdrawal amount must be positive.")

    def display_balance(self):
        """Displays the current balance."""
        print(f"\nAccount balance: ₱{self.balance:.2f}")

    def get_bank_code(self):
        """Accessing protected member."""
        return self._bank_code

    def set_pin(self):
        """Setter method for private PIN."""
        new_pin = input("Enter new 4-digit PIN: ")
        if len(new_pin) == 4 and new_pin.isdigit():
            self.__pin = new_pin
            print("\nPIN updated successfully!")
        else:
            print("\nInvalid PIN format. Please enter a 4-digit number.")

    def get_pin(self):
        """Getter method for private PIN (not recommended in real banking)."""
        return self.__pin


account_number = input("Enter account number: ")
owner = input("Enter account owner's name: ")

while True:
    try:
        initial_balance = float(input("Enter initial deposit amount: "))
        if initial_balance < 0:
            print("Initial deposit cannot be negative.")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter a valid number.")

account = BankAccount(account_number, owner, initial_balance)

while True:
    print("\nChoose an option:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. View Bank Code (Protected)")
    print("5. Change PIN (Private)")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        try:
            amount = float(input("Enter deposit amount: "))
            account.deposit(amount)
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    elif choice == "2":
        try:
            amount = float(input("Enter withdrawal amount: "))
            account.withdraw(amount)
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    elif choice == "3":
        account.display_balance()

    elif choice == "4":
        print(f"\nBank Code: {account.get_bank_code()}")

    elif choice == "5":
        account.set_pin()

    elif choice == "6":
        print("\nThank you for using our banking system!")
        break

    else:
        print("\nInvalid choice. Please enter a number between 1 and 6.")
