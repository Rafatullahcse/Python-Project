class BankAccount:
    def __init__(self, initial_balance):
        self.balance = initial_balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")

    def get_balance(self):
        return self.balance


def main():
    initial_balance = float(input("Enter the initial balance: $"))
    account = BankAccount(initial_balance)

    while True:
        print("\n1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            amount = float(input("Enter the deposit amount: $"))
            account.deposit(amount)
        elif choice == "2":
            amount = float(input("Enter the withdrawal amount: $"))
            account.withdraw(amount)
        elif choice == "3":
            print(f"Current balance: ${account.get_balance():.2f}")
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid option. Try again!")


if __name__ == "__main__":
    main()
