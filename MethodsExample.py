# class and its methods
class Ship:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.cargo = 0

    def sail(self):
        print("{} has sailed!".format(self.name))


# function
def sail_function(name):
    print("{} has sailed!".format(name))