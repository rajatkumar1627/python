largest_So_Far = -1
print("Before", largest_So_Far)
for the_num in [9,5,12,45,8,62,55]:
    if the_num > largest_So_Far:
        largest_So_Far = the_num
    print(largest_So_Far,the_num)

print("After", largest_So_Far)