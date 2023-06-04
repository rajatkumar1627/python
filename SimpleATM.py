# operations
DEPOSIT = "DEPOSIT"
WITHDRAW = "WITHDRAW"
DISPLAY = "DISPLAY"

# read the data
card_number = input("Enter card number: ")
input_pin = input("Enter PIN: ")

# card_pin and card_balance are read from the database

# check that the pin is correct
if card_pin == input_pin:
    # ask the client what they want to do
    action = input("Enter desired action: ")
    if action == DEPOSIT:
        money = float(input("Enter the sum to DEPOSIT: "))
        card_balance += money
        print("Deposited: $", money)
        print("Current balance:", card_balance)
    elif action == WITHDRAW:
        money = float(input("Enter the sum to WITHDRAW: "))
        card_balance -= money
        print("Withdrawn: $", money)
        print("Current balance:", card_balance)
    elif action == DISPLAY:
        print("Current balance:", card_balance)
    else:
        ...
else:
    print("Incorrect pin!")