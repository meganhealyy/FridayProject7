class BankAccount:
    def __init__(self, account_number):
        """Initialize the bank account with an account number and a starting balance of 0."""
        self.account_number = account_number  # Store the account number
        self.balance = 0  # Initialize the balance to 0

    def deposit(self, amount):
        """Deposit money into the account."""
        if amount > 0:  # Check if the deposit amount is valid
            self.balance += amount  # Increase the balance by the deposit amount
            print(f"Deposited ${amount}. New balance is ${self.balance}.")
        else:
            print("Deposit amount must be positive!")

    def withdraw(self, amount):
        """Withdraw money from the account."""
        if 0 < amount <= self.balance:  # Check if the withdrawal amount is valid
            self.balance -= amount  # Decrease the balance by the withdrawal amount
            print(f"Withdrew ${amount}. New balance is ${self.balance}.")
        else:
            print("Insufficient funds or invalid withdrawal amount!")

    def check_balance(self):
        """Return the current balance."""
        return self.balance


# Create an instance of the BankAccount class with an example account number
account = BankAccount("123456789")

# Start an indefinite loop for user interaction
while True:
    print("\nWelcome to your bank account!")
    account_number_input = input("Please enter your account number (or 'exit' to quit): ")
    
    if account_number_input.lower() == "exit":  # Check if the user wants to exit
        print("Thank you for using the banking system. Goodbye!")
        break  # Exit the loop

    # Verify if the entered account number matches the account's number
    if account_number_input == account.account_number:
        print("Options:")
        print("a) Deposit money")
        print("b) Withdraw money")
        print("c) Check balance")

        option = input("Choose an option (a/b/c): ").lower()

        if option == 'a':
            amount = float(input("Enter the amount to deposit: "))
            account.deposit(amount)  # Call the deposit method
        elif option == 'b':
            amount = float(input("Enter the amount to withdraw: "))
            account.withdraw(amount)  # Call the withdraw method
        elif option == 'c':
            balance = account.check_balance()  # Call the check balance method
            print(f"Your current balance is: ${balance}.")
        else:
            print("Invalid option. Please try again.")
    else:
        print("Account number does not match. Please try again.")
