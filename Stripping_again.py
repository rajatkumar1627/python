word = "Mississippi"

# starting from the right side, all "i", "p", and "s" are removed:
print(word.rstrip("ips"))

# the word starts with "M" rather than "i", "p", or "s", so no chars are removed from the left side:
print(word.lstrip("ips"))

# "M", "i", "p", and "s" are removed from both sides, so nothing is left:
print(word.strip("Mips")) # blank
