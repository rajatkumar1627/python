materials = ["water", "milk", "coffee beans", "disposable cups", "money"]
balances = [400, 540, 120, 9, 550]
espresso = [250, 0, 16, 1, 4]
latte = [350, 75, 20, 1, 7]
cappuccino = [200, 100, 12, 1, 6]

def status():
    print("The coffee machine has:")
    for b in range(4):
        print(balances[b], "of", materials[b])
    print("$" + str(balances[4]), "of money")

def calculate(cname):
    global balances
    for c in range(4):
        if balances[c] < cname[c]:
            print("Sorry, not enough", materials[c] + "!")
            return
    print("I have enough resources, making you a coffee!")
    for d in range(4):
        balances[d] -= cname[d]
    balances[4] += cname[4]

def buy():
    print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
    coffee = input()
    if coffee == "1":
        calculate(espresso)
    elif coffee == "2":
        calculate(latte)
    elif coffee == "3":
        calculate(cappuccino)
    else:
        return

def fill():
    global balances
    for f in range(4):
        print("Write how many ml of", materials[f], "do you want to add:")
        balances[f] += int(input())

def take():
    global balances
    print("I gave you $" + str(balances[4]), materials[4])
    balances[4] = 0

while True:
    print("Write action (buy, fill, take, remaining, exit):")
    action = input()
    print()
    if action == "buy":
        buy()
    elif action == "fill":
        fill()
    elif action == "take":
        take()
    elif action == "remaining":
        status()
    elif action == "exit":
        break
    print()