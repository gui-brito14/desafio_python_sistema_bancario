# Welcome message when the program starts
print("Welcome to the Bank System!\nWe are glad to have you here.\nWhat would you like to do today?")

# Menu with numbered options
menu = """

[1] Deposit
[2] Withdraw
[3] Statement
[4] Change Limit
[5] Quit

=> """

# Initial variables
balance = 0
limit = 500
statement = ""
withdraw_count = 0
WITHDRAW_LIMIT = 3
total_withdrawn = 0  # Total amount withdrawn so far
limit_change_count = 0
MAX_LIMIT_CHANGE = 3
MAX_LIMIT = 1500

# Main system loop
while True:

    option = input(menu)

    if option == "1":  # Option for deposit
        amount = float(input("Enter deposit amount: "))

        if amount > 0:
            confirm = input(f"Confirm deposit of $ {amount:.2f}? (y/n): ")
            if confirm.lower() == 'y':
                balance += amount
                statement += f"Deposit: $ {amount:.2f}\n"
                print(f"Deposit of $ {amount:.2f} completed successfully!\n")
            else:
                print("Operation cancelled.\n")

        else:
            print("Operation failed! The entered amount is invalid.\n")

        print("Is there anything else I can help you with?\n")

    elif option == "2":  # Option for withdrawal
        amount = float(input("Enter withdrawal amount: "))

        exceeded_balance = amount > balance
        exceeded_limit = amount > limit
        exceeded_withdrawals = withdraw_count >= WITHDRAW_LIMIT

        if exceeded_balance:
            print("Operation failed! Insufficient funds.\n")

        elif exceeded_limit:
            print("Operation failed! Withdrawal amount exceeds the limit.\n")

        elif exceeded_withdrawals:
            print("Operation failed! Maximum number of withdrawals exceeded.\n")

        elif amount > 0:
            confirm = input(f"Confirm withdrawal of $ {amount:.2f}? (y/n): ")
            if confirm.lower() == 'y':
                balance -= amount
                statement += f"Withdrawal: $ {amount:.2f}\n"
                withdraw_count += 1
                total_withdrawn += amount  # Update total withdrawn
                print(f"Withdrawal of $ {amount:.2f} completed successfully!\n")

                # Remaining withdrawals and limit after withdrawal
                remaining_withdrawals = WITHDRAW_LIMIT - withdraw_count
                remaining_limit = limit - amount

                print(f"You have {remaining_withdrawals} withdrawals remaining.\n")
                print(f"You can withdraw up to $ {remaining_limit:.2f} without exceeding the limit.\n")

            else:
                print("Operation cancelled.\n")

        else:
            print("Operation failed! The entered amount is invalid.\n")

        print("Is there anything else I can help you with?\n")

    elif option == "3":  # Option for statement
        print("\n================ STATEMENT ================")
        print("No transactions made." if not statement else statement)
        print(f"\nBalance: $ {balance:.2f}")
        print("==========================================\n")

        print("Is there anything else I can help you with?\n")

    elif option == "4":  # Option to change limit
        if limit_change_count < MAX_LIMIT_CHANGE:
            print(f"Your current limit is: $ {limit:.2f}\n")
            new_limit = float(input("Enter the new limit (max 1500): "))

            if new_limit > MAX_LIMIT:
                print("Operation failed! The maximum limit is $1500.\n")
            elif new_limit <= total_withdrawn:
                print(f"Operation failed! You have already withdrawn an amount greater than or equal to $ {new_limit:.2f}.\n")
            else:
                confirm = input(f"Confirm new limit of $ {new_limit:.2f}? (y/n): ")
                if confirm.lower() == 'y':
                    limit = new_limit
                    limit_change_count += 1
                    print(f"Limit changed to $ {new_limit:.2f} successfully!\n")
                else:
                    print("Operation cancelled.\n")
        else:
            print("Operation failed! You have reached the limit change maximum.\n")

        print("Is there anything else I can help you with?\n")

    elif option == "5":  # Option to quit
        break

    else:
        print("Invalid operation, please select the desired operation again.\n")

# Goodbye message when the program ends
print("Thank you for using our system. Goodbye!\nPlease come back whenever you need.")