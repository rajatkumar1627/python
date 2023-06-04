input_str = input("Enter a string: ")

for char in input_str:
    if not char.isalpha():
        break
    if char.lower() in 'aeiou':
        print("vowel")
    else:
        print("consonant")