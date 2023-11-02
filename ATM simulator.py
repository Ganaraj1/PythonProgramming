class ATM:
    def __init__(self, balance=0):
        self.balance = balance

    def check_balance(self):
        return f"Your account balance is {self.balance}$"

    def deposit(self, amount):
        self.balance += amount
        return f"{amount}$ has been deposited. Your new balance is {self.balance}$"

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return f"You have withdrawn {amount}$. Your new balance is {self.balance}$"
        else:
            return "Insufficient funds. Withdrawal failed."

def main():
    atm = ATM()
    while True:
        print("\nWelcome to the ATM")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Quit")
        choice = input("Please select an option (1, 2, 3, or 4): ")

        if choice == '1':
            print(atm.check_balance())
        elif choice == '2':
            amount = float(input("Enter the amount to deposit: "))
            print(atm.deposit(amount))
        elif choice == '3':
            amount = float(input("Enter the amount to withdraw: "))
            print(atm.withdraw(amount))
        elif choice == '4':
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please select options 1, 2, 3, or 4.")

if __name__ == '__main__':
    main()
