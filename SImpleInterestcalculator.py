def calculate(amount, interest_rate, time):
    interest = (amount * interest_rate * time) / 100
    total_amount = amount + interest
    return interest, total_amount


def print_result(interest, total_amount):
    print("The interest is:", interest)
    print("The total amount is:", total_amount)


amount = float(input())
interest_rate = float(input())
time = int(input())
interest, total_amount = calculate(amount, interest_rate, time)
print_result(interest, total_amount)
