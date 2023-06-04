phrase = "Let it be"


def global_printer():
    print(phrase)  # we can use phrase because it's a global variable


global_printer()  # Let it be is printed
print(phrase)  # we can also print it directly

phrase = "Hey Jude"

global_printer()  # Hey Jude is now printed because we changed the value of phrase


def printer():
    local_phrase = "Yesterday"
    print(local_phrase)  # local_phrase is a local variable


printer()  # Yesterday is printed as expected

print(local_phrase)  # NameError is raised
