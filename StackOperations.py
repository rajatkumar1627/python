class Stack:
    def __init__(self):
        self.stack = []  # Using a list to store the elements

    def push(self, el):
        self.stack.append(el)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return None  # Return None if stack is empty

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return None  # Return None if stack is empty

    def is_empty(self):
        return len(self.stack) == 0
