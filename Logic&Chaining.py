a = 1
b = 2
c = 3
e = 4
f = 5
g = 6

# True and-expressions return the result of the last operation:
print(b + c * f >= e and (f + g) * c)  # (17 >= 4 is True) and 33 -> 33
print((f + g) * c and b + c * f >= e)  # 33 and (17 >= 4 is True) -- > True

# False and-expressions return a boolean False value:
print(b + c * f <= e and (f + g) * c)  # (17 <= 4 is False) and 33 --> False
print((f + g) * c and b + c * f <= e)  # 33 and (17 <= 4 is False) --> False

# True or-expressions return the result of the first operation:
print(b + c * f >= e or (f + g) * c)  # (17 >= 4 is True) or 33 --> True
print((f + g) * c or b + c * f >= e)  # 33 or (17 >= 4 is True) --> 33

# True-False or-expressions return the True part:
print((f + g) * c or b + c * f <= e)  # 33 or (17 <= 4 is False) --> 33
print(b + c * f <= e or (f + g) * c)  # (17 <= 4 is False) or 33 --> 33