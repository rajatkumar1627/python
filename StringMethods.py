message = "namaste and welcome to Patna!"
# Strings are immutable

print(message.upper())
# `message` is not changed
print(message)

title_message = message.title()
# `title_message` contains a new string
# with the first character of each word capitalized
print(title_message)

upper_message = message.upper()
print(upper_message)

message_lower = message.lower()
print(message_lower)

message_capitalize = message.capitalize()
print(message_capitalize)

message_swap = message.swapcase()
print(message_swap)

print(message.replace("Patna", "Gaya"))

replaced_message = message.replace("o", "!", 2)
print(replaced_message)

# again, the source string is unchanged, only its copy is modified
print(message)


print("----------------------------------")
sentence = "London is the capital of Great Britain."
sentence = sentence.lower()
sentence.upper()
sentence = sentence.replace("a", "x", 2)
sentence.capitalize()
print(sentence)