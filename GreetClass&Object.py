class Person:
    def __init__(self, name):
        self.name = name

    # create the method greet here
    def greet(self):
        return "Hello, I am {}!".format(self.name)
# Read the name from input
name = input()

# Create an instance of the Person class with the input name
person = Person(name)

# Call the greet method on the person instance and print the result
print(person.greet())