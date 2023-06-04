angle_one = int(input("Enter angle 1: "))
angle_two = int(input("Enter angle 2: "))
angle_three = int(input("Enter angle 3: "))

if angle_one + angle_two + angle_three == 180 and angle_one > 0 and angle_two > 0 and angle_three > 0:
    print("The triangle is valid!")
else:
    print("The triangle is not valid!")
