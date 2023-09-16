import os
import matplotlib.pyplot as plt


class ATM:
    def __init__(self):
        self.users = []
        self.accounts = []
        self.current_user_index = None

    def add_user(self, name, pin):
        if any(user['name'] == name for user in self.users):
            print("User already exists.")
        else:
            self.users.append({'name': name, 'pin': pin})
            self.accounts.append({'balance': 0})
            with open(f"{name}.txt", "w") as user_file:
                user_file.write(f"Name: {name}\nPIN: {pin}\nBalance: 0")
            print("User created successfully!")

    def login(self, name, pin):
        for idx, user in enumerate(self.users):
            if user['name'] == name and user['pin'] == pin:
                self.current_user_index = idx
                return True
        return False

    def display_balance(self):
        user = self.users[self.current_user_index]
        with open(f"{user['name']}.txt", "r") as user_file:
            data = user_file.read()
            print(data)

    def deposit(self, amount):
        user = self.users[self.current_user_index]
        self.accounts[self.current_user_index]['balance'] += amount
        with open(f"{user['name']}.txt", "a") as user_file:
            user_file.write(f"\nDeposited ${amount}")
        print(f"Deposited ${amount}")

    def withdraw(self, amount):
        user = self.users[self.current_user_index]
        balance = self.accounts[self.current_user_index]['balance']

        if amount > 1000:
            print("Maximum withdrawal limit is $1000 per transaction.")
        elif amount % 10 != 0:
            print("Withdrawal amount must be a multiple of $10.")
        elif amount > balance:
            print("Insufficient balance.")
        else:
            self.accounts[self.current_user_index]['balance'] -= amount
            with open(f"{user['name']}.txt", "a") as user_file:
                user_file.write(f"\nWithdrawn ${amount}")
            print(f"Withdrew ${amount}")

    def plot_account_balances(self):
        user_names = [user['name'] for user in self.users]
        balances = [account['balance'] for account in self.accounts]

        plt.figure(figsize=(8, 6))
        plt.bar(user_names, balances, color='orange')
        plt.xlabel('User')
        plt.ylabel('Balance')
        plt.title('Account Balances')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()


def main():
    atm = ATM()

    while True:
        print("1. Create User")
        print("2. Login")
        print("3. Admin Login")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter your username: ")
            pin = input("Enter a 4-digit PIN: ")
            if len(pin) == 4 and pin.isdigit():
                atm.add_user(name, pin)
            else:
                print("Invalid PIN. Please enter a 4-digit PIN.")

        elif choice == '2':
            name = input("Enter your username: ")
            pin = input("Enter your PIN: ")
            if atm.login(name, pin):
                print("Login successful!")
                while True:
                    print("1. Display Balance")
                    print("2. Deposit")
                    print("3. Withdraw")
                    print("4. Logout")
                    option = input("Enter your option: ")

                    if option == '1':
                        atm.display_balance()

                    elif option == '2':
                        amount = float(input("Enter the amount to deposit: $"))
                        atm.deposit(amount)

                    elif option == '3':
                        amount = float(input("Enter the amount to withdraw: $"))
                        atm.withdraw(amount)

                    elif option == '4':
                        print("Logged out.")
                        break

            else:
                print("Invalid credentials.")

        elif choice == '3':
            admin_name = input("Enter admin username: ")
            admin_pin = input("Enter admin PIN: ")
            if admin_name == "SysAdmin" and admin_pin == "1357":
                print("Admin login successful!")
                while True:
                    print("1. Add User")
                    print("2. Delete User")
                    print("3. Plot Account Balances")
                    print("4. Logout")
                    admin_option = input("Enter your option: ")

                    if admin_option == '1':
                        name = input("Enter the new user's name: ")
                        pin = input("Enter a 4-digit PIN for the new user: ")
                        if len(pin) == 4 and pin.isdigit():
                            atm.add_user(name, pin)
                        else:
                            print("Invalid PIN. Please enter a 4-digit PIN.")

                    elif admin_option == '2':
                        user_to_delete = input("Enter the name of the user to delete: ")
                        user_file_path = f"{user_to_delete}.txt"
                        if os.path.exists(user_file_path):
                            os.remove(user_file_path)
                            print(f"User {user_to_delete} deleted successfully!")
                        else:
                            print(f"User {user_to_delete} not found.")

                    elif admin_option == '3':
                        atm.plot_account_balances()

                    elif admin_option == '4':
                        print("Admin logged out.")
                        break
            else:
                print("Admin login failed.")

        elif choice == '4':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
