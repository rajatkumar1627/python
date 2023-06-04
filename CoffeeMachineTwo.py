def check_resources(water, milk, coffee_beans, cups):
    cups_possible = min(water // 200, milk // 50, coffee_beans // 15)
    if cups_possible > cups:
        return f"Yes, I can make that amount of coffee and even {cups_possible - cups_needed} more than that"
    elif cups_possible == cups:
        return f"Yes, I can make that amount of coffee"
    else:
        return f"No, I can make only {cups_possible} cups of coffee"

# Get user input for available resources
water = int(input("Enter the amount of water (in ml): "))
milk = int(input("Enter the amount of milk (in ml): "))
coffee_beans = int(input("Enter the amount of coffee beans (in g): "))

# Get user input for required number of cups
cups_needed = int(input("Enter the number of cups needed: "))

# Check resources and print the result
result = check_resources(water, milk, coffee_beans, cups_needed)
print(result)

