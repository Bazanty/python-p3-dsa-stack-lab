class Stack:

    def __init__(self, items=None, limit=100):
        # Initialize stack with items and set a limit for the stack
        if items is None:
            items = []
        self.items = items
        self.limit = limit

    def isEmpty(self):
        # Returns True if the stack is empty, False otherwise
        return len(self.items) == 0

    def push(self, item):
        # Adds an item to the stack if it's not full
        if self.full():
            raise IndexError("Stack is full")
        self.items.append(item)

    def pop(self):
        # Removes and returns the top item from the stack
        if self.isEmpty():
            return None
        return self.items.pop()

    def peek(self):
        # Returns the top item without removing it
        if self.isEmpty():
            return None
        return self.items[-1]
    
    def size(self):
        # Returns the number of items in the stack
        return len(self.items)

    def full(self):
        # Returns True if the stack is full, False otherwise
        return len(self.items) >= self.limit

    def search(self, target):
        # Returns the position of the target in the stack or -1 if not found
        try:
            return len(self.items) - self.items.index(target) - 1
        except ValueError:
            return -1
