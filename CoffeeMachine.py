# Write your code here
print("Starting to make a coffee")
print("Grinding coffee beans")
print("Boiling water")
print("Mixing boiled water with crushed coffee beans")
print("Pouring coffee into the cup")
print("Pouring some milk into the cup")
print("Coffee is ready!")

# Get the number of cups of coffee needed from the user
num_cups = int(input("Write how many cups of coffee you will need: "))

# Calculate the amounts of water, milk, and coffee beans needed
water = num_cups * 200  # 200 ml of water per cup
milk = num_cups * 50   # 50 ml of milk per cup
coffee_beans = num_cups * 15  # 15 g of coffee beans per cup

# Print the amounts of water, milk, and coffee beans needed
print(f"For {num_cups} cups of coffee you will need:")
print(f"{water} ml of water")
print(f"{milk} ml of milk")
print(f"{coffee_beans} g of coffee beans")
