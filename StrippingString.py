whitespace_string = "     hey      "
normal_string = "relentless"

print(whitespace_string)
print(normal_string)

# delete spaces from the left side
print(whitespace_string.lstrip())

# delete all "i" and "s" from the left side
print(normal_string.lstrip("re"))

# delete spaces from the right side
print(whitespace_string.rstrip())

# delete all "r" and "s" from the right side
print(normal_string.rstrip("rs)"))

# no spaces from both sides
print(whitespace_string.strip())

# delete all trailing "i" and "s" from both sides
print(normal_string.strip("is"))