num_units = int(input())
if num_units < 1:
    category = "no army"
elif num_units <= 9:
    category = "few"
elif num_units <= 49:
    category = "pack"
elif num_units <= 499:
    category = "horde"
elif num_units <= 999:
    category = "swarm"
else:
    category = "legion"
print(category)