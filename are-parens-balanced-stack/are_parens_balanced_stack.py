# Implement a stack class and check if parents in a string are balanced

class Stack(object):

    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.items is None:
            return None
        else:
            return self.items.pop()

    def is_empty():
        return self.items == []
        # returns true if empty, false if not empty

    def peek(self):
        if if self.items.is_empty():
            return None
        else:
            return self.items[-1]


def are_parens_balanced(str):

    parens = Stack()

    for char in str:
        
        if char == "(":
            parens.push(char)
        elif char == ")":
            if parens.is_empty(): 
                return False # Returns false if first paren is closing paren
            parens.pop()

    return parens.is_empty()

