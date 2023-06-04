number_of_halls = int(input("Enter number of halls: "))
capacity = int(input("Enter capacity of a hall: "))
number_of_viewers = int(input("Enter number of viewers: "))

total_capacity = number_of_halls * capacity

print(total_capacity >= number_of_viewers)